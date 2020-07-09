"""Unittest tests for the Comparator Algorithm."""

# Flask imports
from flask import current_app, url_for
from flask_testing import TestCase

# App instance imports
from main import app

# Test data imports
from context import set_user, set_markets, set_products, set_markets_loc
from context import full_prod, half_prod, one_market_all_prod, two_markets_all_prod
from context import some_prod, no_prod, one_same_prod, one_dif_prod, set_quantity

from responses import res_redirect, res_full_prod, res_half_prod
from responses import res_one_market_all_prod, res_two_markets_all_prod
from responses import res_some_prod, res_no_prod, res_one_same_prod, res_one_dif_prod


class MainTest(TestCase):
    def setUp(self):
        """Initialize all the values the tests will use."""
        self.user_info = set_user()
        self.markets_id = set_markets()
        self.products = set_products()
        self.markets_loc = set_markets_loc()
        self.quantity = set_quantity()

    def create_app(self):
        """Switch to test mode."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_redirect(self):
        """Redirect test using the GET method."""
        response = self.client.get(url_for('comparator'))
        self.assertEquals(response.json, res_redirect())

    def test_full_products(self):
        """Test all supermarkets with all products."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, full_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_full_prod())

    def test_half_products(self):
        """Test all supermarkets with half products."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, half_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_half_prod())

    def test_one_market_all_products(self):
        """Test one supermarket with all products."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, one_market_all_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_one_market_all_prod())

    def test_two_markets_all_products(self):
        """Test two supermarkets with all products."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, two_markets_all_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_two_markets_all_prod())

    def test_some_products(self):
        """Test all supermarkets with some products."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, some_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_some_prod())

    def test_no_products(self):
        """Test all supermarkets with no propducts."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, no_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_no_prod())

    def test_one_same_product(self):
        """Test all supermarkets with only one same product."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, one_same_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_one_same_prod())

    def test_one_dif_product(self):
        """Test all supermarkets with only one diferent product."""
        fake_data = {'cart': [self.user_info, self.markets_id, self.markets_loc, self.products, self.quantity, one_dif_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res_one_dif_prod())
