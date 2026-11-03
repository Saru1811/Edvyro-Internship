
from flask import Flask, request, jsonify, session
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "replace-this-with-a-random-secret"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = True  # Local HTTP testing only
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)

# Demo only: store one user's hashed password in memory
users = {}

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid request"}), 400

    username = data.get("username")
    password = data.get("password")

    # Server-side input validation
    if not isinstance(username, str) or not username.strip():
        return jsonify({"error": "Invalid input"}), 400

    if not isinstance(password, str) or len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    if len(username) > 50 or len(password) > 128:
        return jsonify({"error": "Input too long"}), 400

    if username in users:
        return jsonify({"error": "Registration failed"}), 409

    # Never store the plain-text password
    users[username] = generate_password_hash(password)

    return jsonify({"message": "Registration successful"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid request"}), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify({"error": "Invalid username or password"}), 401

    stored_hash = users.get(username)

    if stored_hash and check_password_hash(stored_hash, password):
     session.clear()
    session["username"] = username
    session.permanent = True
    return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid username or password"}), 401

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200


if __name__ == "__main__":
    app.run(debug=False)
