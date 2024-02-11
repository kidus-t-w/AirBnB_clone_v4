#!/usr/bin/python3
"""A Flask application designed to create a comprehensive HTML page
 featuring dropdown menus for selecting locations and amenities,
   along with listings of available rentals."""
from flask import Flask, render_template
from models import storage
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/2-hbnb')
def display_hbnb():
    """Create a webpage featuring a
      dropdown menu for states and cities."""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('2-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
