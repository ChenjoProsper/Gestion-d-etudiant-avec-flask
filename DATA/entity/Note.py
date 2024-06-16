from ..setting import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etudiant_id = db.Column(db.Integer, db.ForeignKey('etudiant.id'), nullable=False)
    matiere_id = db.Column(db.Integer, db.ForeignKey('matiere.id'), nullable=False)
    note = db.Column(db.Float, nullable=False)