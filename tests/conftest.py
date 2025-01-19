import pytest
import os

from ticket_api import db
from ticket_api import create_app
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def client():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URL')
    app.testing = True
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()