"""Unittest tests for the Comparator Algorithm."""


# Flask imports
from flask import current_app, url_for
from flask_testing import TestCase

# App instance imports
from main import app

# Test data imports
import context as ctx
import responses as res


class MainTest(TestCase):
    def setUp(self):
        """Initialize all the values the tests will use."""
        self.maxDiff = None

    def create_app(self):
        """Switch to test mode."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_redirect(self):
        """Redirect test using the GET method."""
        response = self.client.get(url_for('comparator'))
        self.assertEquals(response.json, res.redirect())

    def test_full_products(self):
        """Test all supermarkets with all products."""
        fake_data = {'cart': [ctx.full_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.full_prod())

    def test_half_products(self):
        """Test all supermarkets with half products."""
        fake_data = {'cart': [ctx.half_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.half_prod())

    def test_one_market_all_products(self):
        """Test one supermarket with all products."""
        fake_data = {'cart': [ctx.one_market_all_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.one_market_all_prod())

    def test_two_markets_all_products(self):
        """Test two supermarkets with all products."""
        fake_data = {'cart': [ctx.two_markets_all_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.two_markets_all_prod())

    def test_some_products(self):
        """Test all supermarkets with some products."""
        fake_data = {'cart': [ctx.some_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.some_prod())

    def test_no_products(self):
        """Test all supermarkets with no propducts."""
        fake_data = {'cart': [ctx.no_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.no_prod())

    def test_one_same_product(self):
        """Test all supermarkets with only one same product."""
        fake_data = {'cart': [ctx.one_same_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.one_same_prod())

    def test_one_dif_product(self):
        """Test all supermarkets with only one diferent product."""
        fake_data = {'cart': [ctx.one_dif_prod()]}
        response = self.client.post(url_for('comparator'), json=fake_data)
        self.assertEquals(response.json, res.one_dif_prod())
