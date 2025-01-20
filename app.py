from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
import random

# Initialising the Flask app and the SocketIO object
app = Flask(__name__)
socketio = SocketIO(app)

# python dictionary to store connected users. Key is socket id and value is username
users = {}

@app.route('/')
def index():
    return render_template('index.html')

# We are listening for the 'connect' event
@socketio.on('connect')
def handle_connect():
    # Create variables for the current user
    username = f"User_{random.randint(1000,9999)}"
    gender = random.choice(["girl", "boy"])
    avatar_url = f" https://avatar.iran.liara.run/public/{gender}?username={username}"

    # Store the user in the users dictionary
    users[request.sid] = {"username": username, "avatar": avatar_url}   
    # Notify all users that a new user has joined using the broadcast attribute
    emit("user_joined", {"username": username, "avatar": avatar_url}, broadcast=True)
    emit("set_username", {"username": username})
    
# For Disconnection
@socketio.on('disconnect')
def handle_disconnect():
    # Pop the user from the users dictionary
    user = users.pop(request.sid, None)
    if user:
        emit("user_left", {"username":user["username"]}, broadcast=True)
        
# For Chat Message
@socketio.on("send_message")
def handle_message(data):
    user = users.get(request.sid)
    # When we recieve the user we get user avatar, username and message
    if user:
        emit("new_message", {"username": user["username"], "avatar": user["avatar"], "message": data["message"]}, broadcast=True)
        
# For Update
@socketio.on("update_username")
def handle_update_username(data):
    old_username = users[request.sid]["username"]
    new_username = data["username"]
    users[request.sid]["username"] = new_username
    
    emit("username_updated", {
        "old_username": old_username,
        "new_username": new_username,
    }, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)