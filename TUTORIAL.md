# Tutorial: Reproducible Setup for Local Chat App

## Prerequisites
- Python 3.10+
- Git

## Step-by-Step Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/fairyfemirins/local-chat-app.git
   cd local-chat-app
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask flask-socketio geopy
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Access the app:**
   Open `http://localhost:5014` in your browser.

## Testing the App
1. Open two browser tabs at `http://localhost:5014`.
2. Allow location access in both tabs.
3. Send a message in one tab and verify it appears in the other.

## Troubleshooting
- **Port already in use:** Change the port in `app.py` (e.g., `port=5015`).
- **Location access denied:** Manually set latitude/longitude in the browser console:
  ```javascript
  socket.emit('update_location', { user_id: userId, latitude: 37.7749, longitude: -122.4194 });
  ```