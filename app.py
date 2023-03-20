"""Flask app for Cupcakes"""

import os

from flask import Flask, flash, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.get("/api/cupcakes")
def list_all_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

# @app.get("/api/cupcakes/<int:cupcake_id>"):
# def list_single_cupcake(cupcake_id):

# @app.post("/api/cupcakes"):
# def create_cupcake():

