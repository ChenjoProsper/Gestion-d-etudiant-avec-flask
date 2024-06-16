from ..setting import db
from ..entity.Etudiant import Etudiant
from ..entity.Note import Note
from .CrudNote import supprimerNote
from Metier.funtion import moyenne,saisir

def ajoutEtudiant(nom,prenom,age,niveau):
    etu = Etudiant(nom=nom,prenom=prenom,age=age,niveau=niveau)
    db.session.add(etu)
    db.session.commit()
    print("Ajouter")

def modifierEtudiant(id):
    try:
        etu = Etudiant.query.get_or_404(id)
        etu.nom = input("Nom: ")
        etu.prenom = input("Prenom: ")
        etu.age = saisir("Age: ")
        etu.niveau = saisir("Niveau: ")
        db.session.commit()
        print("Modifier")
    except:
        print("Une erreur a ete rencontrer")

def supprimerEtudiant(id):
    try:
        etu = Etudiant.query.get_or_404(id)
        noteEtu = Note.query.filter_by(etudiant_id=id)
        for note in noteEtu:
            supprimerNote(note.id)
        db.session.delete(etu)
        db.session.commit()
        print("Supprimer")
    except:
        print("Une erreur a ete rencontrer")

def rechercherEtudiant(id):
    try:
        print("-----------------------------")
        etu = Etudiant.query.get_or_404(id)
        print("Id: {}".format(etu.id))
        print("Nom: {}".format(etu.nom))
        print("Prenom: {}".format(etu.prenom))
        print("Age: {}".format(etu.age))
        print("Niveau: {}".format(etu.niveau))
        print("Moyenne: {}".format(moyenne(id)))
        print("-----------------------------")
    except:
        print("Une erreur a ete rencontrer")

def afficherEtudiant():
    etudiants = Etudiant.query.all()
    for etu in etudiants:
        print("-----------------------------")
        print("Id: {}".format(etu.id))
        print("Nom: {}".format(etu.nom))
        print("Prenom: {}".format(etu.prenom))
        print("Age: {}".format(etu.age))
        print("Niveau: {}".format(etu.niveau))
        print("Moyenne: {}".format(moyenne(etu.id)))
        print("-----------------------------")