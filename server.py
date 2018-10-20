from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for)

from flask_debugtoolbar import DebugToolbarExtension

from datetime import datetime, timedelta

from google_sheet import get_all_rows_from_db

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

################################################################################

################### VIEW FUNCTIONS RENDERING TEMPLATES #########################

@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html')

@app.route('/d3')
def d3():

  return render_template('d3_viz.html')

@app.route('/graph.json')
def graph():

  # temporary until we get database
  rows = get_all_rows_from_db()

  children = []
  for row in rows:
    child = {}

    child["name"] = row["sender_first_name"]

    child_children = []
    child_children.append({"name": row["admiree_1_first_name"], "size": 50000})
    if row["admiree_2_first_name"]:
      child_children.append({"name": row["admiree_2_first_name"], "size": 50000})
    if row["admiree_3_first_name"]:
      child_children.append({"name": row["admiree_3_first_name"], "size": 50000})

    child["children"] = child_children
    child["size"] = 50000

    children.append(child)
    
  data = { "name": "",
            "children": children}


  return jsonify(data)


if __name__ == "__main__":

    app.debug = True

    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()

    # app.run(port=5000, threaded=True, host='0.0.0.0')