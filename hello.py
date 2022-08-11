from flask import Flask

app = Flask(__name__)

@app.route('/users/<string:username>')
def hello_world(username='MyName'):
    return("Hello {}!".format(username))

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='https://onshushind.herokuapp.com', port=81)
