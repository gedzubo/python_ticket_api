import os

from flask import Flask, jsonify
from dotenv import load_dotenv
from ticket_api.db import db
from ticket_api.models.ticket_option import TicketOption
from ticket_api.presenters.ticket_option_presenter import TicketOptionPresenter

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEVELOPMENT_DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.sort_keys = False

    db.init_app(app)

    # GET /ticket_options/:id
    @app.route("/ticket_options/<uuid:id>", methods=["GET"])
    def show_ticket_option(id):
        ticket_option = TicketOption.query.get(id)
        print(ticket_option)
        if ticket_option is None:
            return jsonify({ 'message': 'Not found' }), 404
        else:
            return TicketOptionPresenter(ticket_option).present()

    return app