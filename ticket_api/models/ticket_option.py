from ticket_api import db

class TicketOption(db.Model):
    __tablename__ = "ticket_options"

    id = db.Column(db.Uuid, primary_key=True)
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    allocation = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<TicketOption {self.id}>'