from app import app
from extensions import db
from models import User

with app.app_context():

    admin = User(
        name="Admin",
        email="admin@gmail.com",
        password="admin123",
        role="admin"
    )

    teacher = User(
        name="Teacher",
        email="teacher@gmail.com",
        password="teacher123",
        role="teacher"
    )

    student = User(
        name="Student",
        email="student@gmail.com",
        password="student123",
        role="student"
    )

    db.session.add(admin)
    db.session.add(teacher)
    db.session.add(student)

    db.session.commit()

    print("Sample users inserted successfully!")
