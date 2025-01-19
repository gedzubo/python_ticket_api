import uuid

from ticket_api import db
from datetime import datetime

class TicketOption(db.Model):
    __tablename__ = "ticket_options"

    id = db.Column(db.Uuid, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    allocation = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<TicketOption {self.id}>'