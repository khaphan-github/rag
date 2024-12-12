from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
  UPLOAD_DIR = os.getenv('UPLOAD_DIR', '/default/upload/dir')
  DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')
  DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
  CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
  QDRANT_CLIENT_URL = os.getenv('QDRANT_CLIENT_URL')
  QDRANT_CLIENT_API_KEY = os.getenv('QDRANT_CLIENT_API_KEY')
settings = Settings()