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


@app.route("/comparator/", methods=['POST'])
def comparator():
    try:
        user = request.args.get('user')
        cart = request.args.get('cart')

        if user and cart:
            return jsonify({'body': 'Everything is OK'})
        else:
            return jsonify({'body': 'Invalid information'})

    except Exception:
        return jsonify({'body': 'Invalid information'})
