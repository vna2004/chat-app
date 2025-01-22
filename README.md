# 💎Python Chat App

This is a real-time chat application built using Flask and Socket.IO. The app allows users to join with a randomly generated username and avatar, send messages, update their username, and leave the chat seamlessly.

⚙️View the site at : https://chat-app-1-fn4m.onrender.com

## ⭐Features
- **Real-Time Messaging**: Leverages Socket.IO for instantaneous message broadcasting.
- **Dynamic Usernames and Avatars**: Users are assigned unique usernames and avatars on connection.
- **Username Updates**: Users can update their usernames during the session.
- **User Join and Leave Notifications**: Keeps all participants informed about who joins or leaves the chat.

## 🔎Prerequisites
- Python 3.7+
- Flask
- Flask-SocketIO

## 🔮User Interface
![Image](https://github.com/user-attachments/assets/54e066be-8178-4cff-9846-6887d48dc20f)

## 🔗Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install required packages:
   ```bash
   pip install flask flask-socketio
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open a web browser and go to `http://localhost:5000/` to start chatting!

```

## Output
When a user connects, they receive a randomly generated username like `User_1234` and an avatar URL. Messages sent by any user are broadcasted to all connected clients in real time.

