"""Flask app for Cupcakes"""

import os
from flask import Flask, request, jsonify, redirect, render_template
from models import db, connect_db, Cupcake, DEFAULT_IMG_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get("/")
def show_homepage():
    """Shows the homepage with list of cupcakes and add cupcake form."""

    return redirect("static/base.html")

@app.get("/api/cupcakes")
def list_all_cupcakes():
    """Return all cupcakes
    JSON {'cupcakes': [{id, flavor, size, rating, image},...]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def list_single_cupcake(cupcake_id):
    """Return cupcake
    JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """Create cupcake from posted JSON data & return it.

    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake_info(cupcake_id):
    """Update a cupcake.

    Returns JSON {'cupcake': {id, flavor, size, rating, image}}"""

    curr_cupcake = Cupcake.query.get_or_404(cupcake_id)

    curr_cupcake.flavor = request.json.get("flavor", curr_cupcake.flavor)
    curr_cupcake.size = request.json.get("size", curr_cupcake.size)
    curr_cupcake.rating = request.json.get("rating", curr_cupcake.rating)
    curr_cupcake.image = request.json.get("image", curr_cupcake.image)

    #add note here
    if not curr_cupcake.image:
        curr_cupcake.image = DEFAULT_IMG_URL

    db.session.commit()

    serialized = curr_cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete a cupcake.

    Returns JSON {"deleted": cupcake_id}"""

    curr_cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(curr_cupcake)
    db.session.commit()

    return jsonify(deleted=cupcake_id)




