from flask import Flask, jsonify, request
# from models import TicketOption

app = Flask(__name__)

# GET /ticket_options/:id
@app.route("/ticket_options/<uuid:id>", methods=["GET"])
def show_ticket_option():
    return "<p>Ticket Option {ticket_option_id}!</p>"