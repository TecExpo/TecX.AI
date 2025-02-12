from backend.fastapi.models import User
from backend.database.sql.schema import SessionLocal

db = SessionLocal()

def test_create_and_fetch_user():
    user = User(email="integration@example.com", password="hashedpassword")
    db.add(user)
    db.commit()

    fetched_user = db.query(User).filter(User.email == "integration@example.com").first()
    assert fetched_user is not None
    assert fetched_user.email == "integration@example.com"
