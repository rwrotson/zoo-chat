import os
import json
from dotenv import load_dotenv


DOTENV_PATH = ''
load_dotenv(DOTENV_PATH)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

MESSAGES_PATH = 'messages.json'
with open(MESSAGES_PATH, 'r') as f:
    MESSAGES = json.load(f)
