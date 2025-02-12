import pytest
from backend.fastapi.models import User
from backend.database.sql.schema import engine, SessionLocal

db = SessionLocal()

def test_create_user():
    user = User(email="testuser@example.com", password="hashedpassword")
    db.add(user)
    db.commit()

    retrieved_user = db.query(User).filter(User.email == "testuser@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.email == "testuser@example.com"

def test_user_not_found():
    user = db.query(User).filter(User.email == "nonexistent@example.com").first()
    assert user is None
