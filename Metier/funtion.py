from DATA.entity.Note import Note
from DATA.entity.Matiere import Matiere
from DATA.entity.Etudiant import Etudiant
from DATA.setting import db
from DATA.dao.CrudNote import supprimerNote

def get_matiere(matiere_id):
    return Matiere.query.get(matiere_id)

def moyenne(id):
    notes = Note.query.filter_by(etudiant_id=id)
    somme = 0
    total = 0
    for note in notes:
        matiere = get_matiere(note.matiere_id)  # Récupère l'objet matiere
        somme += note.note * matiere.credit
        total += matiere.credit
    if (total != 0):
        return somme/total
    else:
        return 0

def monterNiveau(id):
    try:
        etud = Etudiant.query.get_or_404(id)
        if(moyenne(id)>=10):
            etud.niveau += 1
            db.session.commit()
            print("L'etudiant {} est passe au niveau {}".format(etud.nom,etud.niveau))
            noteEtu = Note.query.filter_by(etudiant_id=id)
            for note in noteEtu:
                supprimerNote(note.id)
        else:
            print("L'etudiant {} ne peut pas passer au niveau superieur sa moyenne est {}".format(etud.nom,moyenne(id)))
    except:
        print("Une erreur est survenu")

def orientation(id):
    try:
        notes = Note.query.filter_by(etudiant_id=id)
        max = notes[0]
        for note in notes:
            if(note.note > max.note):
                max = note
        matiere = get_matiere(max.matiere_id)
        print("Il serait favorable pour voue d'aller faire {}".format(matiere.nom))
    except:
        print("Une erreur est survenu")


def saisir(phrase):
    while(1):
        try:
            print(phrase,end="")
            saisie = int(input())
            return saisie
        except:
            print("Veuillez saisir un nombre entier")