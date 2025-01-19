import pytest

from ticket_api.models.ticket_option import TicketOption
from ticket_api import db


def test_show_ticket_option(client):
    ticket_option = TicketOption(
        name="General Admission",
        desc="General Admission ticket",
        allocation=100
    )
    db.session.add(ticket_option)
    db.session.commit()

    res = client.get(f'/ticket_options/{ticket_option.id}')
    assert res.status_code == 200
    assert res.json == {
        'id': str(ticket_option.id),
        'name': 'General Admission',
        'desc': 'General Admission ticket',
        'allocation': 100
    }