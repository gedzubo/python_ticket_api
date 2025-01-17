class TicketOptionPresenter:
    def __init__(self, object):
        self.object = object

    def present(self):
        return {
            'id': self.o.id,
            'name': self.object.name,
            'price': self.object.price,
            'description': self.object.description,
            'quantity': self.object.quantity,
            'event_id': self.object.event_id,
        }