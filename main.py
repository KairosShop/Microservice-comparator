"""Main file of the Microservice."""


# Flask imports
from flask import request, jsonify, redirect, url_for
import unittest
from flask_cors import CORS

# App instance import
from app import create_app

# Database import
from flask_sqlalchemy import SQLAlchemy

# Test data imports
from tests.context import full_prod, half_prod, one_market_all_prod, set_quantity
from tests.context import two_markets_all_prod, some_prod, no_prod, markets_ids, products_ids
from tests.context import one_same_prod, one_dif_prod, markets_images, products_images

from tests.context import set_user, set_markets, set_products, set_markets_loc

# Comparator Algorithm import
from comparator.comparator import the_comparator

# Cart data imports
from loader.data import get_json_cart
from loader.loader import json_loader

# Pandas import
import pandas as pd


app = create_app()

db = SQLAlchemy(app)

CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


# This part connects the microservice with the database

# POST
#   - userId
#   - latitud
#   - longitud

# user = [userId, [latitud, longitud]]

try:
    cart = db.Table('Orders', db.metadata, autoload=True, autoload_with=db.engine)
    results = db.session.query(cart).all()
    # print(results[5]) # Users
    # print(results)

except Exception as e:
    print(f"Error while trying to get the table. : {e} Doesn't exist.")


@app.cli.command()
def test():
    """Set the unittest loader."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    """Handles the 404 error."""
    return jsonify({'error': 'false', 'status': '200', 'body': 'Not found'})


@app.errorhandler(405)
def not_allowed(error):
    """Handles the 405 error."""
    return jsonify({'error': 'false', 'status': '200', 'body': 'Method not allowed'})


@app.errorhandler(500)
def server_error(error):
    """Handles the 500 error."""
    return jsonify({'error': 'false', 'status': '200', 'body': 'Server error'})


@app.route("/")
def home():
    """Handles the root redirection."""
    return redirect(url_for('comparator'))


@app.route("/comparator/", methods=['GET', 'POST'])
def comparator():
    """Handles the Comparator Algorithm."""
    try:
        if request.method == 'POST':
            cart = request.args.get('cart')

            if app.config['TESTING'] == True:
                test = request.get_json('cart')

                context = the_comparator(
                    set_user(),
                    set_markets(),
                    set_markets_loc(),
                    set_products(),
                    set_quantity(),
                    test['cart'][5],
                    markets_images(),
                    products_images(),
                    markets_ids(),
                    products_ids()
                )

                return jsonify({
                    'error': 'false',
                    'status': '200',
                    'body': context}
                )

            if cart:
                # This part will load the data from the database
                id = 1
                products, quantity = json_loader(id, get_json_cart)

                user_info = set_user()
                markets_id = set_markets()
                markets_loc = set_markets_loc()
                products = set_products()
                quantity = set_quantity()
                
                price = {
                    '0001': full_prod(),
                    '0002': half_prod(),
                    '0003': one_market_all_prod(),
                    '0004': two_markets_all_prod(),
                    '0005': some_prod(),
                    '0006': no_prod(),
                    '0007': one_same_prod(),
                    '0008': one_dif_prod()
                }

                try:
                    prices = price[cart]

                except Exception:
                    return jsonify({
                        'error': 'false',
                        'status': '200',
                        'body': 'Invalid information'
                    })

                context = the_comparator(
                    user_info,
                    markets_id,
                    markets_loc,
                    products,
                    quantity,
                    prices,
                    markets_images(),
                    products_images(),
                    markets_ids(),
                    products_ids()
                )

                return jsonify({
                    'error': 'false',
                    'status': '200',
                    'body': context
                })

            else:
                return jsonify({
                    'error': 'false',
                    'status': '200',
                    'body': 'There is no information'
                })

        else:
            return jsonify({
                'error': 'false',
                'status': '200', 
                'body': {
                    'message': 'Welcome to the Comparator Microservice',
                    'method': 'Try again with the POST method',
                    'value': '/comparator/?cart=<cart_id>'
                }
            })

    except Exception:
        return jsonify({
            'error': 'false',
            'status': '200',
            'body': 'Wrong information'
        })
