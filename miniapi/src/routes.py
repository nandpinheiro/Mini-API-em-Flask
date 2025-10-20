from flask import Blueprint, jsonify, request

user_bp = Blueprint('user_bp', __name__)

users = [
    {"id": 1, "name": "Fernando", "email": "fernando@example.com"}
]

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users.append(new_user)
    return jsonify(new_user), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200