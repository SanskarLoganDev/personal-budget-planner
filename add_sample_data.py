from app import create_app, db
from app.models import User, Category, Transaction
from datetime import datetime

app = create_app()

with app.app_context():
    # Add sample user
    user1 = User(username="john_doe", email="john@example.com", password_hash="hashedpassword")
    db.session.add(user1)
    
    # Commit the user to generate the user_id
    db.session.commit()

    # Add sample categories
    income_category = Category(name="Salary", type="income")
    expense_category = Category(name="Groceries", type="expense")
    db.session.add(income_category)
    db.session.add(expense_category)

    # Commit the categories to generate their IDs
    db.session.commit()

    # Add sample transactions using the committed user_id and category_id
    transaction1 = Transaction(user_id=user1.id, category_id=income_category.id, amount=5000, date=datetime.utcnow(), description="Monthly salary")
    transaction2 = Transaction(user_id=user1.id, category_id=expense_category.id, amount=150, date=datetime.utcnow(), description="Grocery shopping")
    db.session.add(transaction1)
    db.session.add(transaction2)

    # Commit the transactions to the database
    db.session.commit()
