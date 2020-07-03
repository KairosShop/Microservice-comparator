from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    # Test if the app exists
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    # Test if the app is on test mode
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    # Test if the app rejects the GET method
    def test_comparator_get(self):
        response = self.client.get(url_for('comparator'))
        self.assert405(response)

    # Test if the app can handle the POST method
    def test_comparator_post(self):
        fake_data = {'user': 'user', 'cart': 'cart'}
        response = self.client.post(url_for('comparator'), data=fake_data)
        self.assert200(response)
