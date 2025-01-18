class TicketOptionPresenter:
    def __init__(self, object):
        self.object = object

    def present(self):
        return {
            'id': self.object.id,
            'name': self.object.name,
            'desc': self.object.desc,
            'allocation': self.object.allocation,
        }