# wait_for_db.py
import time
import sys
from django.db import connections
from django.db.utils import OperationalError

def wait_for_db():
    max_retries = 10
    retry_delay = 5  # seconds
    for _ in range(max_retries):
        try:
            connections['default'].ensure_connection()
            print("Database is ready!")
            return True
        except OperationalError:
            print("Waiting for database...")
            time.sleep(retry_delay)
    print("Database not ready after max retries.")
    return False

if __name__ == "__main__":
    if not wait_for_db():
        sys.exit(1)