"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#default url if image is not passed
DEFAULT_IMG_URL = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    flavor = db.Column(
        db.String(40),
        nullable=False
    )

    size = db.Column(
        db.String(40),
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )

    image = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMG_URL
    )

    def serialize(self):
        """Serialize to dictionary"""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }