from flask import Flask
from os import path
import os


def create_app():
	app = Flask(__name__)
	brand_secret_key_value = os.environ.get('BRAND_SECRET_KEY', None)
	app.config['SECRET_KEY'] = brand_secret_key_value

	from .views import views

	app.register_blueprint(views, url_prefix="/")

	return app