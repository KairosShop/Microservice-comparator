# General imports
from flask import request, jsonify, redirect, url_for
import unittest

# App instance imports
from app import create_app

# Auxiliary imports
from comparator.context import get_context


app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'body': 'Not found'})


@app.errorhandler(405)
def not_allowed(error):
    return jsonify({'body': 'Method not allowed'})


@app.errorhandler(500)
def server_error(error):
    return jsonify({'body': 'Server error'})


@app.route("/")
def home():
    return redirect(url_for('comparator'))


@app.route("/comparator/", methods=['GET', 'POST'])
def comparator():
    try:
        if request.method == 'POST':
            cart = request.args.get('cart')

            if cart:
                context = get_context()
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
