"""Main file of the Microservice."""


# Flask imports
from flask import request, jsonify, redirect, url_for
import unittest
from flask_cors import CORS

# App instance import
from app import create_app

# Database import
from flask_sqlalchemy import SQLAlchemy

# Comparator Algorithm import
from comparator.comparator import the_comparator

# Cart data imports
from loader.loader import test_loader, loader

# Pandas import
import pandas as pd


app = create_app()

db = SQLAlchemy(app)

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# This part connects the microservice with the database
try:
    cart = db.Table('Orders', db.metadata, autoload=True, autoload_with=db.engine)
    results = db.session.query(cart).all()

except Exception as e:
    print(f"Error while trying to get the {e} table. It doesn't exist.")


@app.cli.command()
def test():
    """Set the unittest loader."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    """Handles the 404 error."""
    
    return jsonify({
        'error': 'false',
        'status': '200',
        'body': 'Not found'
    })


@app.errorhandler(405)
def not_allowed(error):
    """Handles the 405 error."""
    
    return jsonify({
        'error': 'false',
        'status': '200',
        'body': 'Method not allowed'
    })


@app.errorhandler(500)
def server_error(error):
    """Handles the 500 error."""
    
    return jsonify({
        'error': 'false',
        'status': '200',
        'body': 'Server error'
    })


@app.route("/")
def home():
    """Handles the root redirection."""
    return redirect(url_for('comparator'))


@app.route("/comparator/", methods=['GET', 'POST'])
def comparator():
    """Handles the Comparator Algorithm."""
    try:
        # POST method conditional
        data = {}

        if request.method == 'POST':

            if app.config['TESTING'] == True:
                # Testing structure
                req = request.get_json('id')
                test = test_loader(req)
                
                context = the_comparator(*test)
            
            else:
                # Server running structure
                data['id'] = request.args.get('id')            
                data['lat'] = request.args.get('lat')
                data['lon'] = request.args.get('lon')

                if data['id']:
                    try:
                        load = loader(**data)

                    except Exception:
                        return jsonify({
                            'error': 'false',
                            'status': '200',
                            'body': 'Invalid information'
                        })

                    context = the_comparator(*load)

                else:
                    return jsonify({
                        'error': 'false',
                        'status': '200',
                        'body': 'There is no information'
                    })
                
            return jsonify({
                    'error': 'false',
                    'status': '200',
                    'body': context
                })

        # GET method conditional
        else:
            return jsonify({
                'error': 'false',
                'status': '200', 
                'body': {
                    'message': 'Welcome to the Comparator Microservice',
                    'method': 'Try again with the POST method',
                    'value': '/comparator/?id=<user_id>&lat=<user_latitude>&lon=<user_longitud>'
                }
            })

    except Exception:
        return jsonify({
            'error': 'false',
            'status': '200',
            'body': 'Something wrong has happen'
        })
