# Local Chat App

## Overview
A **location-based chat app** that connects users in the same area (e.g., within 1km).
- **Anonymous:** No login required.
- **Real-time:** WebSocket-based messaging.
- **Privacy-focused:** No persistent data, auto-delete after 24h.

## Technical Architecture
- **Backend:** Flask + Flask-SocketIO + SQLite.
- **Frontend:** HTML/CSS/JS + Bootstrap.
- **Location:** Geopy for distance calculations.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/fairyfemirins/local-chat-app.git
   cd local-chat-app
   ```
2. Install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open `http://localhost:5014` in your browser.

## Usage
- Allow location access when prompted.
- Chat with users within 1km.

## License
MIT License.