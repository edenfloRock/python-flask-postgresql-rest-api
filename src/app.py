from flask import Flask
from flask_cors import CORS
from config import config

# Routes
from routes import Movie

app = Flask(__name__)

#CORS(app,resources={"*":{"origins":"http://localhost:3000"}})
CORS(app,resources={"*":{"origins":"http://localhost:9300"}}) #Webpack

def page_not_found(error):
    return "<h1>Not page found</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Movie.main, url_prefix = '/api/movies' )

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()