import os
import time
import socket

def wait_for_db():
    host = os.getenv("DATABASE_HOST", "db")
    port = int(os.getenv("DATABASE_PORT", 3306))
    retry_count = 0
    max_retries = 10
    while retry_count < max_retries:
        try:
            with socket.create_connection((host, port), timeout=5):
                print(f"Database is available at {host}:{port}")
                return
        except socket.error:
            print(f"Database is not available yet, retrying... ({retry_count + 1}/{max_retries})")
            retry_count += 1
            time.sleep(5)
    print("Failed to connect to the database. Exiting.")
    exit(1)

if __name__ == "__main__":
    wait_for_db()
