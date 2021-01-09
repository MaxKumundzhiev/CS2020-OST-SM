import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

DB_NAME = 'ost'
DB_URI = 'mongodb://admin:secret@localhost:27888/?authSource=admin'

NAS = './NAS/'
