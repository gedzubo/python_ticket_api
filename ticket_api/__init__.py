import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEVELOPMENT_DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # GET /ticket_options/:id
    @app.route("/ticket_options/<uuid:id>", methods=["GET"])
    def show_ticket_option(id):
        return jsonify({"id": id})

    return app