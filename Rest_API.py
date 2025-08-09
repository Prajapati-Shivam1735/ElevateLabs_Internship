from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}
next_id = 1

# GET - Fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET - Fetch a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# POST - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    users[next_id] = {
        'id': next_id,
        'name': data['name'],
        'email': data['email']
    }
    next_id += 1
    return jsonify(users[next_id - 1]), 201

# PUT - Update existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    if not data:
        return jsonify({'error': 'Invalid data'}), 400
    
    users[user_id].update(data)
    return jsonify(users[user_id])

# DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
