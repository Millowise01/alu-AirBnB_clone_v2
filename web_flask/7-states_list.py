#!/usr/bin/python3
"""
Starts a Flask web application to display states from the database.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the session after each request """
    try:
        storage.close()
    except Exception as e:
        app.logger.error(f"Error closing storage session: {e}")


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays a list of states from the database in alphabetical order.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
