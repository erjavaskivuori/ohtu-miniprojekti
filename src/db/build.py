import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
# pylint: disable=C0413
from db.initialize import initialize_database


def build():
    initialize_database()


if __name__ == "__main__":
    build()
