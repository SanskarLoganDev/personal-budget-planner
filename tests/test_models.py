import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import create_app, db
from app.models import User, Category, Transaction
from config_test import TestConfig
from datetime import datetime

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.app = create_app()
        self.app.config.from_object(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        """Tear down test environment"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        """Test user creation"""
        user = User(username="john_doe", email="john@example.com", password_hash="hashedpassword")
        db.session.add(user)
        db.session.commit()
        self.assertTrue(User.query.filter_by(username="john_doe").first())

    def test_transaction_model(self):
        """Test transaction creation"""
        user = User(username="john_doe", email="john@example.com", password_hash="hashedpassword")
        db.session.add(user)
        category = Category(name="Salary", type="income")
        db.session.add(category)
        db.session.commit()

        transaction = Transaction(user_id=user.id, category_id=category.id, amount=5000, date=datetime.utcnow(), description="Monthly salary")
        db.session.add(transaction)
        db.session.commit()

        self.assertTrue(Transaction.query.filter_by(amount=5000).first())

if __name__ == '__main__':
    unittest.main()
