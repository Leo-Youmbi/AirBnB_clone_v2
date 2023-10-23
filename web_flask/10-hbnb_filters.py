#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity

app = Flask('web_flask')


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    """Route /hbnb_filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    # print(amenities)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Closes db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
