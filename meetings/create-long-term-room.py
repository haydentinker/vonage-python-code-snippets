import os
from datetime import datetime, timedelta
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get('VONAGE_APPLICATION_PRIVATE_KEY_PATH')

ROOM_DISPLAY_NAME = os.environ.get('ROOM_DISPLAY_NAME')
EXPIRATION_DATE = (datetime.utcnow() + timedelta(days=30)).isoformat()

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

params = {
    'display_name': ROOM_DISPLAY_NAME,
    'type': 'long_term',
    'expires_at': EXPIRATION_DATE,
}

response = client.meetings.create_room(params)
