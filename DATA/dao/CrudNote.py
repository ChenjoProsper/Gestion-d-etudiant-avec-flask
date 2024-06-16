from ..setting import db
from ..entity.Note import Note

def ajouterNote(etu_id,mat_id,note):
    try:
        note = Note(etudiant_id=etu_id,matiere_id=mat_id,note=note)
        db.session.add(note)
        db.session.commit()
        print("Ajouter")
    except:
        print("Une erreur est survenu")

def modifierNote(etud_id,mat_id):
    try:
        note = Note.query.filter_by(etudiant_id=etud_id,matiere_id = mat_id).first()
        note.note = float(input("Note: "))
        db.session.commit()
        print("Modifier")
    except:
        print("Une erreur a ete rencontrer")

def supprimerNote(etud_id,mat_id):
    try:
        note = Note.query.filter_by(etudiant_id=etud_id,matiere_id = mat_id).first()
        db.session.delete(note)
        db.session.commit()
        print("Supprimer")
    except:
        pass
