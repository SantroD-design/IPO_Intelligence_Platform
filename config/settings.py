import os

# -----------------------------------
# Project Root Directory
# -----------------------------------

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -----------------------------------
# Database
# -----------------------------------

DATABASE_FOLDER = os.path.join(PROJECT_ROOT, "database")

DATABASE_PATH = os.path.join(DATABASE_FOLDER, "ipo.db")

# -----------------------------------
# Data Folders
# -----------------------------------

DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

RAW_DATA_FOLDER = os.path.join(DATA_FOLDER, "raw")

PROCESSED_DATA_FOLDER = os.path.join(DATA_FOLDER, "processed")

ARCHIVE_FOLDER = os.path.join(DATA_FOLDER, "archive")

# -----------------------------------
# Export Folder
# -----------------------------------

EXPORT_FOLDER = os.path.join(PROJECT_ROOT, "exports")

# -----------------------------------
# Log Folder
# -----------------------------------

LOG_FOLDER = os.path.join(PROJECT_ROOT, "logs")