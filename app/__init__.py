from config import DevConfig
from config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    #We create a create_app() function that takes the configuration setting key as an argument. 
    
# Initializing application
    app = Flask(__name__)


     # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Will add the views and forms

     # setting config
    from .request import configure_request
    configure_request(app)

    return app   

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')


# from app import views