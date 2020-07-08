"""Basic Unittest tests."""


# Flask imports
from flask_testing import TestCase
from flask import current_app, url_for

# App instance imports
from main import app


class MainTest(TestCase):
    def create_app(self):
        """Switch to test mode."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exists(self):
        """Test if the app exists."""
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        """Test if the app is in test mode."""
        self.assertTrue(current_app.config['TESTING'])

    def test_comparator_get(self):
        """Test the GET method status."""
        response = self.client.get(url_for('comparator'))
        self.assert200(response)

    def test_comparator_post(self):
        """Test the POST method status."""
        fake_data = {'cart': '0001'}
        response = self.client.post(url_for('comparator'), data=fake_data)
        self.assert200(response)
