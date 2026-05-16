#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from geopy.distance import geodesic
import sqlite3
import uuid
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initialize SQLite database
conn = sqlite3.connect('messages.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id TEXT PRIMARY KEY,
        room TEXT,
        user_id TEXT,
        message TEXT,
        timestamp INTEGER
    )
''')
conn.commit()

# Temporary storage for user locations
user_locations = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    user_id = str(uuid.uuid4())
    emit('assign_user_id', {'user_id': user_id})

@socketio.on('update_location')
def handle_location(data):
    user_id = data['user_id']
    latitude = data['latitude']
    longitude = data['longitude']
    user_locations[user_id] = (latitude, longitude)
    
    # Find nearby users (within 1km)
    nearby_users = []
    for uid, (lat, lon) in user_locations.items():
        if uid != user_id:
            distance = geodesic((latitude, longitude), (lat, lon)).km
            if distance <= 1.0:  # 1km radius
                nearby_users.append(uid)
    
    # Join rooms for nearby users
    for uid in nearby_users:
        join_room(f'room_{uid}')
    
    emit('nearby_users', {'nearby_users': nearby_users})

@socketio.on('send_message')
def handle_message(data):
    user_id = data['user_id']
    message = data['message']
    room = f'room_{user_id}'
    
    # Store message in SQLite
    msg_id = str(uuid.uuid4())
    timestamp = int(time.time())
    cursor.execute('''
        INSERT INTO messages (id, room, user_id, message, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (msg_id, room, user_id, message, timestamp))
    conn.commit()
    
    # Broadcast message to room
    emit('receive_message', {
        'user_id': user_id,
        'message': message,
        'timestamp': timestamp
    }, room=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5014, debug=True, allow_unsafe_werkzeug=True)