"""Main file of the Microservice."""


# Flask imports
from flask import request, jsonify, redirect, url_for
import unittest

# App instance imports
from app import create_app

# Test data imports
from tests.context import set_user, set_markets, set_products, set_markets_loc
from tests.context import full_prod, half_prod, one_market_all_prod
from tests.context import two_markets_all_prod, some_prod, no_prod
from tests.context import one_same_prod, one_dif_prod

# Comparator Algorithm imports
from comparator.comparator import the_comparator


app = create_app()


@app.cli.command()
def test():
    """Set the unittest loader."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    """Handles the 404 error."""
    return jsonify({'body': 'Not found'})


@app.errorhandler(405)
def not_allowed(error):
    """Handles the 405 error."""
    return jsonify({'body': 'Method not allowed'})


@app.errorhandler(500)
def server_error(error):
    """Handles the 500 error."""
    return jsonify({'body': 'Server error'})


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
                    test['cart'][0],
                    test['cart'][1],
                    test['cart'][2],
                    test['cart'][3],
                    test['cart'][4]
                )
                
                return jsonify({'body': context})

            if cart:
                user_info = set_user()
                markets_id = set_markets()
                markets_loc = set_markets_loc()
                products = set_products()
                
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
                    return jsonify({'body': 'Invalid information'})

                context = the_comparator(
                    user_info,
                    markets_id,
                    markets_loc,
                    products,
                    prices
                )
                return jsonify({'body': context})

            else:
                return jsonify({'body': 'There is no information'})

        else:
            return jsonify({
                'body': {
                    'message': 'Welcome to the Comparator Microservice',
                    'method': 'Try again with the POST method',
                    'value': '/comparator/?cart=<cart_id>'
                }
            })

    except Exception:
        return jsonify({'body': 'Invalid information'})
