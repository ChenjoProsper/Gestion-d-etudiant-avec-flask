from ..setting import db

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    prenom = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    niveau = db.Column(db.Integer, nullable=False)
    notes = db.relationship('Note', backref='etudiant', lazy=True)

