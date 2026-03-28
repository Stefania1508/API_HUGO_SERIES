from flask import Flask

from app.routes.series_routes import series_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(series_bp)
    return app


app = create_app()
