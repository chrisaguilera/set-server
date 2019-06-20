from setserver import app
from flask import jsonify, request, abort, make_response
from datetime import datetime

users = [
    {
        'username': 'chrisaguilera',
        'password': 'password', 
        'scores': [
            {
            	'user': 'chrisaguilera',
                'score': 1500,
                'date': datetime.now()
            },
            {
            	'user': 'chrisaguilera',
                'score': 2300,
                'date': datetime.now()
            }
        ]
    },
    {
        'username': 'kevin',
        'password': 'password',
        'scores': [
            {
            	'user': 'kevin',
                'score': 2400,
                'date': datetime.now()
            }
        ]
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.route("/api/1.0/users", methods=['GET'])
def get_users():
    return jsonify(users)

@app.route("/api/1.0/newUser", methods=['POST'])
def post_user():
    if request.is_json:
        content = request.json
        user = {
            'username': content['username'],
            'password': content['password'],
            'scores': []
        }
        users.append(user)
        return jsonify(user)

@app.route("/api/1.0/scores", methods=['GET'])
def get_scores():
	scores = []
	for user in users:
		for score in user['scores']:
			scores.append(score)
	return jsonify(scores)

@app.route("/api/1.0/signIn/<string:username>", methods=['POST'])
def signIn(username):
	if request.is_json:
		content = request.json
		if not any(user['username'] == username for user in users):
			abort(404)
		else:
			for user in users:
				if user['username'] == username:
					if user['password'] == content['password']:
						return jsonify(user)
					else:
						abort(404)



