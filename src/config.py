import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(
    dirname, "..", "src", "db", DATABASE_FILENAME)

POPULATE_CITATIONS_PATH = os.path.join(
    dirname, "..", "src", "db", "citations_data.txt")
