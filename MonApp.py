from DATA.setting import app
from DATA.dao.CrudNote import *
from DATA.dao.CrudEtudiant import *
from DATA.dao.CrudMatiere import *
from Metier.funtion import *
import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("\n\n*****************************Menu Principale*****************************\n\n")
        print("1) Enregistrer un nouvel etudiant")
        print("2) Modifier les informations d'un etudiant")
        print("3) Rechercher un etudiant")
        print("4) Supprimer un etudiant")
        print("5) Afficher les etudiants")
        print("6) Enregistrer une nouvelle matiere")
        print("7) Modifier les informations d'une matiere")
        print("8) Rechercher une matiere")
        print("9) Supprimer une matiere")
        print("10) Afficher les matieres")
        print("11) Enregistrer une nouvelle note")
        print("12) Modifier les informations d'une note")
        print("13) Supprimer une note")
        print("14) Faire monter un etudiant de niveau")
        print("15) Orienter un etudiant")
        chx = saisir("Choix: ")
        match chx:
            case 1:
                os.system("clear")
                nom = input("Nom: ")
                prenom = input("Prenom: ")
                age = saisir("Age: ")
                niveau = saisir("Niveau: ")
                ajoutEtudiant(nom,prenom,age,niveau)
            case 2:
                os.system("clear")
                id = saisir("Id: ")
                modifierEtudiant(id)
            case 3:
                os.system("clear")
                id = saisir("Id: ")
                rechercherEtudiant(id)
            case 4:
                os.system("clear")
                id = saisir("Id: ")
                supprimerEtudiant(id)
            case 5:
                os.system("clear")
                afficherEtudiant()
            case 6:
                os.system("clear")
                nom = input("Nom: ")
                credit = saisir("Credit: ")
                ajouterMatiere(nom,credit)
            case 7:
                os.system("clear")
                id = saisir("Id: ")
                modifierMatiere(id)
            case 8:
                os.system("clear")
                id = saisir("Id: ")
                rechercherMatiere(id)
            case 9:
                os.system("clear")
                id = saisir("Id: ")
                supprimerMatiere(id)
            case 10:
                os.system("clear")
                afficherMatiere()
            case 11:
                os.system("clear")
                etu_id = saisir("Id de l'etudiant: ")
                mat_id = saisir("Id de la matiere: ")
                note = saisir("Note: ")
                ajouterNote(etu_id,mat_id,note)
            case 12:
                os.system("clear")
                etu_id = saisir("Id de l'etudiant: ")
                mat_id = saisir("Id de la matiere: ")
                modifierNote(etu_id,mat_id)
            case 13:
                os.system("clear")
                etu_id = saisir("Id de l'etudiant: ")
                mat_id = saisir("Id de la matiere: ")
                supprimerNote(etu_id,mat_id)
            case 14:
                os.system("clear")
                id = saisir("Id: ")
                monterNiveau(id)
            case 15:
                os.system("clear")
                id = saisir("Id: ")
                orientation(id)
    app.run(debug=True)

