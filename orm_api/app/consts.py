import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = 'db'
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

SQLALCHEMY_DB_URL = (
    f'postgresql://'
    f'{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}'
    f'/{POSTGRES_DB}'
)

# postgresql://postgres:buzzword-hgjd736gjd7@db:5432/compatibility