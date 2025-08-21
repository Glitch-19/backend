from flask import Flask, request, session, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "mysecretkey"

# Enable CORS for local development and your deployed frontend
CORS(app, supports_credentials=True, origins=[
    "http://localhost:3000",  # For local React
    "https://frontend-zeta-mauve-71.vercel.app"  # Your deployed frontend
])


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend is running!"})


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == "tanya" and password == "1234":
        session["username"] = username
        return jsonify({"message": "Login successful", "username": username}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route("/api/user", methods=["GET"])
def get_user():
    if "username" in session:
        return jsonify({"username": session["username"]}), 200
    return jsonify({"error": "Not logged in"}), 401


@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return jsonify({"message": "Logged out"}), 200


if __name__ == "__main__":
    app.run(port=5001, debug=True)
