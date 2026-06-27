import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

DATABASE_FOLDER = os.path.join(PROJECT_ROOT, "database")

DATABASE_PATH = os.path.join(DATABASE_FOLDER, "ipo.db")

EXPORT_FOLDER = os.path.join(PROJECT_ROOT, "exports")

LOG_FOLDER = os.path.join(PROJECT_ROOT, "logs")