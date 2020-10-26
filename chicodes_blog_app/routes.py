# Import the app variable from the init
from chicodes_blog_app import app

# Import specific packages from flask
from flask import render_template

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')