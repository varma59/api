from flask import Flask

setup = Flask(__name__)

@setup.route('/')
def index():
    return 'Web App with Python Flask!'

setup.run(host='0.0.0.0', port=81)
