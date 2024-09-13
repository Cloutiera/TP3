#librairies importées
from random import randint
from time import sleep
#variables
vies = 20
force_adversaire = 0
resultat = 0
resultat_adversaire = 0
adversaire = 0
numero_combat = 0
victoires = 0
defaites = 0
streak = 0
continuer_regles = "tgef6tsrgfegrtegrtvgegtrvger6tv6e"
continuer = True
while continuer:
    while vies > 0:
        #informations de départ
        adversaire = adversaire + 1
        print("Vous jouez contre le monstre %d\n"%(adversaire))

        force_adversaire = randint(1,5)
        print("Vous tombez contre un adversaire de difficulté %d\n" %(force_adversaire))

        print("Il vous reste %d vies\n" % (vies))
        print("Vous avez une série de victoires consécutives de %d\n" %(streak))

        print("Vous avez fait %d combats avec %d victoire(s) et %d défaite(s).\n" %(numero_combat, victoires, defaites))
        choix = int(input("Que voulez-vous faire? \n     1 - Combattre cet adversaire\n     2 - Contourner cet adversaire et ouvrir une autre porte (-1 vie)\n     3 - Afficher les règles de jeu\n     4 - Quitter la partie\n"))
        if (choix == 1):
            numero_combat += 1
            print("On lance les dés")
            resultat = randint(1,6)
            sleep(2)
            print("Le résultat est" ,resultat)
            print("on lance les dés de l'adversaire")
            resultat_adversaire = randint(1, 6)
            sleep(2)
            print("le résultat est",resultat_adversaire)
            sleep(2)
            if resultat > resultat_adversaire:
                vies = vies + force_adversaire
                print("Vous avez gagné. Il vous reste %d vies\n\n" % (vies))
                victoires += 1
                streak += 1
                sleep(4)
            else:
                vies = vies - force_adversaire
                print("Vous avez perdu. Il vous reste %d vies\n\n" % (vies))
                defaites += 1
                streak = 0
                sleep(4)
            if (vies <= 0):
                print("La partie est terminée vous avez vaincu %d monstres" % (victoires))
                break

        elif (choix == 2):
            vies = vies - 1
        elif (choix == 3):
            print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0. \nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
            continuer_regles = input("appuyez sur entrée pour continuer")
            while continuer_regles == "tgef6tsrgfegrtegrtvgegtrvger6tv6e":
                sleep(10)
        elif(choix == 4):
            print("Merci et au revoir")
            sleep(3)
            exit()



