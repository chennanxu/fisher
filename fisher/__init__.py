from flask import Flask
from views import view


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.secure')
    app.config.from_object('config.setting')
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(view)
    app.config.update(dict(
        SECRET_KEY="powerful secretkey"
    ))
    return app

from views import book