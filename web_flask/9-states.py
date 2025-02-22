#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """Closes the storage session."""
    storage.close()

@app.route('/states', strict_slashes=False)
def states():
    """Displays a list of all states."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """Displays details of a specific state and its cities."""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html', state=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
