import threading
from backend.fastapi.models import User
from backend.database.sql.schema import SessionLocal

db = SessionLocal()

def insert_user():
    user = User(email=f"loadtest{threading.get_ident()}@example.com", password="hashedpassword")
    db.add(user)
    db.commit()

def test_database_load():
    threads = []
    for _ in range(50):  # Simulate 50 parallel database transactions
        thread = threading.Thread(target=insert_user)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
