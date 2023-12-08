from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return "Error", 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' in data and 'lastname' in data:
        user = {
            'id': len(users) + 1,
            'name': data['name'],
            'lastname': data['lastname']
        }
        users.append(user)
        return jsonify(user), 201
    else:
        return "Error", 400

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.get_json()
        if 'name' in data:
            user['name'] = data['name']
        if 'lastname' in data:
            user['lastname'] = data['lastname']
        return '', 204
    else:
        return "Error", 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def replace_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.get_json()
        user['name'] = data['name']
        user['lastname'] = data['lastname']
        return '', 204
    else:
        return "Error", 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
