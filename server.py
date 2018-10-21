from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for)

from flask_debugtoolbar import DebugToolbarExtension

from datetime import datetime, timedelta

from google_sheet import get_all_rows_from_db

from helper import get_adjectives

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

    adjs1 = get_adjectives("1", row)
    adjs2 = get_adjectives("2", row)
    adjs3 = get_adjectives("3", row)

    child_children = []
    child_children.append({"name": row["admiree_1_first_name"], "size": 50000, "adjectives": adjs1})
    if row["admiree_2_first_name"]:
      child_children.append({"name": row["admiree_2_first_name"], "size": 50000, "adjectives": adjs2})
    if row["admiree_3_first_name"]:
      child_children.append({"name": row["admiree_3_first_name"], "size": 50000, "adjectives": adjs3})

    child["children"] = child_children
    child["size"] = 50000

    children.append(child)
    
  data = { "name": "",
            "children": children}

  return jsonify(data)

@app.route('/words.json')
def words():

  rows = get_all_rows_from_db()

  compliments = []

  for row in rows:
    compliments.append(row["admiree_1_adjective_1"])
    compliments.append(row["admiree_1_adjective_2"])
    compliments.append(row["admiree_1_adjective_3"])
    compliments.append(row["admiree_2_adjective_1"])
    compliments.append(row["admiree_2_adjective_2"])
    compliments.append(row["admiree_2_adjective_3"])
    compliments.append(row["admiree_3_adjective_1"])
    compliments.append(row["admiree_3_adjective_2"])
    compliments.append(row["admiree_3_adjective_3"])

  compliment_string = " ".join(compliments)

  return jsonify(compliment_string)

@app.route("/word_cloud")
def word_cloud():

  return render_template("word_cloud.html")


if __name__ == "__main__":

    app.debug = True

    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()

    # app.run(port=5000, threaded=True, host='0.0.0.0')