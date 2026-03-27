from flask import Flask
from app.routes.series_routes import series_bp
from app import create_app 

app = create_app() 

if __name__ == "__main__":
    app.run(debug=True)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(series_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)