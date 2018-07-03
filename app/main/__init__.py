from flask import Flask
from flask_bootstrap import Bootstrap

#Initialize flask extensions
bootstrap = Bootstrap

def create_app(config_name):
    app = Flask(__name__)
    
    return app



