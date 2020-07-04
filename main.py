from flask import request, jsonify
import unittest

from app import create_app


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
    return jsonify({'body': {
        'message': 'Welcome to the Combinator Microservice',
        'goto': '/comparator/'}})


@app.route("/comparator/", methods=['GET', 'POST'])
def comparator():
    try:
        if request.method == 'POST':
            cart = request.args.get('cart')
            markets = request.args.get('markets')

            context = {
                'user': 'user_id',
                'all_in_one': {
                    'supermarket1': {'total_products': 5, 'total_sum': 10},
                    'supermarket2': {'total_products': 5, 'total_sum': 12},
                    'supermarket3': {'total_products': 4, 'total_sum': 13}
                },
                'cheapest': {
                    'supermarket1': {'total_products': 2, 'total_sum': 3},
                    'supermarket2': {'total_products': 2, 'total_sum': 4},
                    'supermarket3': {'total_products': 1, 'total_sum': 1}
                },
                'details': {
                    'product1': {'supermarket1': 5, 'supermarket2': 4, 'supermarket3': 5},
                    'product2': {'supermarket1': 4, 'supermarket2': 5, 'supermarket3': 6},
                    'product3': {'supermarket1': 6, 'supermarket2': 4, 'supermarket3': 5},
                    'product4': {'supermarket1': 7, 'supermarket2': 3, 'supermarket3': 7},
                    'product5': {'supermarket1': 5, 'supermarket2': 6, 'supermarket3': 8}
                }
            }

            if cart and markets:
                return jsonify({'body': context})
            else:
                return jsonify({'body': 'There is no information'})
        else:
            return jsonify({
                'body': {
                    'method': 'Try with POST method',
                    'values': '/?cart=<value>&markets=<values>'
                }
            })

    except Exception:
        return jsonify({'body': 'Invalid information'})
