# import the Flask dependency
from flask import Flask

# create a new Flask app instance
app = Flask(__name__)

# define the starting point, also known as the root
@app.route('/')
def count():
    return 'Hello world'