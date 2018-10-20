from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for)

from flask_debugtoolbar import DebugToolbarExtension

from datetime import datetime, timedelta

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

################################################################################

################### VIEW FUNCTIONS RENDERING TEMPLATES #########################

@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html')



if __name__ == "__main__":

    app.debug = True

    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()

    # app.run(port=5000, threaded=True, host='0.0.0.0')