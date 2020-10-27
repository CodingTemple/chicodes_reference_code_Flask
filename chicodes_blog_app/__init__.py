from flask import Flask

# Import the Config Object
from config import Config

app = Flask(__name__)
# Complete the Config cycle for our Flask App
# And Give access to our Database(When we have one)
# Along with our Secret Key
app.config.from_object(Config)