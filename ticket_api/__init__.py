from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # app.config

    # db.init_app(app)

    # GET /ticket_options/:id
    @app.route("/ticket_options/<uuid:id>", methods=["GET"])
    def show_ticket_option(id):
        return jsonify({"id": id})

    return app