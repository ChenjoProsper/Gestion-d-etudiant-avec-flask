from ..setting import db
from ..entity.Matiere import Matiere
from ..entity.Note import Note
from .CrudNote import supprimerNote

def ajouterMatiere(nom,credit):
    mat = Matiere(nom=nom,credit=credit)
    db.session.add(mat)
    db.session.commit()
    print("Ajouter")

def modifierMatiere(id):
    try:
        mat = Matiere.query.get_or_404(id)
        mat.nom = input("Nom: ")
        mat.credit = int(input("Credit: "))
        db.session.commit()
        print("Modifier")
    except:
        print("Une erreur est survenu")

def supprimerMatiere(id):
    try:
        mat = Matiere.query.get_or_404(id)
        noteMat = Note.query.filter_by(matiere_id=id)
        for note in noteMat:
            supprimerNote(note.id)
        db.session.delete(mat)
        db.session.commit()
        print("Supprimer")
    except:
        print("Une erreur est survenu")

def rechercherMatiere(id):
    try:
        print("-----------------------------")
        mat = Matiere.query.get_or_404(id)
        print("Id: {}".format(mat.id))
        print("Nom: {}".format(mat.nom))
        print("Credit: {}".format(mat.credit))
        print("-----------------------------")
    except:
        print("Une erreur est survenu")

def afficherMatiere():
    matieres = Matiere.query.all()
    for mat in matieres:
        print("-----------------------------")
        print("Id: {}".format(mat.id))
        print("Nom: {}".format(mat.nom))
        print("Credit: {}".format(mat.credit))
        print("-----------------------------")