# White Paper: Local Chat App

## Problem Statement
People want to connect with others nearby for casual conversations, local events, or networking, but existing platforms (e.g., Meetup, Nextdoor) require accounts, lack anonymity, or are not real-time.

## Solution
A **location-based chat app** that:
- Connects users within 1km.
- Requires no login (anonymous).
- Uses WebSocket for real-time messaging.
- Stores no persistent data (auto-delete after 24h).

## Design Decisions
1. **Flask + WebSocket:** Lightweight, easy to deploy, and scalable for real-time chat.
2. **SQLite:** Temporary message storage (auto-delete after 24h).
3. **Geopy:** Accurate distance calculations for location-based matching.
4. **Bootstrap:** Responsive frontend for mobile and desktop.

## Future Work
- Add topic-based channels (e.g., "Sports", "Tech").
- Implement moderation tools.
- Integrate with event discovery platforms.

## Conclusion
This app fills a gap for **privacy-focused, local, real-time chat** without the overhead of commercial platforms.