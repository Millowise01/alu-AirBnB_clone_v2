#!/usr/bin/python3
"""
Script that starts a Flask web application:
- The web app listens on 0.0.0.0:5000.
- Uses DBStorage to fetch data.
- Displays a list of states and their cities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays states and cities."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Closes the storage session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
