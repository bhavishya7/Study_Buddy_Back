from database.database import db, ma
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    pronouns = db.Column(db.String(250), nullable=True)
    major = db.Column(db.String(250), nullable=True, default="")
    grad_year = db.Column(db.String(250), nullable=True)
    current_classes = db.Column(db.String(250), nullable=True, default="")
    pref_time = db.Column(db.String(250), nullable=True)
    study_locations = db.Column(db.String(250), nullable=True, default="")
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
