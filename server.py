from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, CheckConstraint, ForeignKey, ARRAY
from flask_marshmallow import Marshmallow


app = Flask(__name__)
connect_to_db(app, os.environ.get("DATABSE_URL"))

# Init db & mm
db = SQLAlchemy(app)
ma = Marshmallow(app)

PORT = int(os.environ.get("PORT",5000))
DEBUG = "NO_DEBUG" not in os.environ

app.run(host="0.0.0.0", port=PORT, debug=DEBUG)

#Routes
@app.route("/error")
def error():
    raise Exception("Error!")

@app.route('/')
def index():
  return '<h1>Landing page</h1>'

@app.route('/signup')
def signup():
  return '<h1>signup page</h1>'

@app.route('/login')
def login():
  return '<h1>login page</h1>'

@app.route('/mapview')
def mapView():
  return '<h1>Current User</h1>'

@app.route('/mapview/<int:id>')
def mapViewId(id):
  return '<h1>User map info by ID</h1>' 'user ID %d' % id

@app.route('/mapview/friends')
def mapViewFriends():
  return '<h1>Friendslist map info of current user</h1>'

@app.route('/friends/list')
def friendsList():
  return '<h1>Get all friends of user by ID</h1>'

@app.route('/friends/list/<int:id>')
def friendsListById(id):
  return '<h1>Friends list by ID</h1>' 'user ID %d' % id

@app.route('/friends/request/send/<int:id>')
def friendRequestSend(id):
  return '<h1>Current user requests another user as a friend</h1>' 'user ID %d' % id

@app.route('/friends/request/accept/<int:id>')
def friendRequestAccept(id):
  return '<h1>Current user accepts another user as a friend</h1>' 'user ID %d' % id

@app.route('/friends/request/decline/<int:id>')
def friendRequestDecline(id):
  return '<h1>Current user decline another user as a friend</h1>' 'user ID %d' % id

@app.route('/users/<username>')
def username(username):
  return '<h1>Get all users with similar name</h1>' 'username %s' % username

@app.route('/users/<int:id>')
def userId(id):
  return '<h1>Get user by ID</h1>' 'user ID %d' % id

@app.route('/users/settings')
def userSettings():
  return '<h1>Get users settings by current User</h1>'

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id): #how can this endpoint be more DRY!!??
  user = users.query.get(id)
  username = request.json['username']
  email = request.json['email']
  first_name = request.json['first_name']
  last_name = request.json['last_name']
  age = request.json['age']
  nationality = request.json['nationality']
  picture_url = request.json['picture_url']
  role = request.json['role']

  user.username = username
  user.email = email
  user.first_name = first_name
  user.last_name = last_name
  user.age = age
  user.nationality = nationality
  user.picture_url = picture_url
  user.role = role

  db.session.commit()
  return user_schema.jsonify(user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = users.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

@app.route('/signout') #CAN BE CHANGED if we decide to use flask-login
def signout(): 
  session.pop('username')
  return redirect(url_for('index'))


if __name__ == "__main__":
  app.run(debug=True)
