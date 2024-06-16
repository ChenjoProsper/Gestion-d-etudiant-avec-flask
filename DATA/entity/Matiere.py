from ..setting import db


class Matiere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    notes = db.relationship('Note', backref='matiere', lazy=True)

