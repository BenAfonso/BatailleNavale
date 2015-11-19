# -*- coding: utf-8 -*-
from Bateau import Bateau
from Grille import Grille
from Position import Position
from EnsBateaux import EnsBateaux
from Resultat import Resultat
from Joueur import Joueur
from Partie import Partie
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def header():
	cls()
	print "================================================================================\n"
	print "==                BEST BATAILLE NAVALE Online v49.8.1 Build 8.1               ==\n"
	print "================================================================================\n"

def demandeNoms():
	header()
	NomJoueur = raw_input("Joueur 1>> Votre nom: ")
	Partie.get_joueur1().set_NomJoueur(NomJoueur)

	NomJoueur = raw_input("Joueur 2>> Votre nom: ")
	Partie.get_joueur2().set_NomJoueur(NomJoueur)

	print "Joueur 1 : "+Partie.get_joueur1().get_NomJoueur()
	print "Joueur 2 : "+Partie.get_joueur2().get_NomJoueur()

# Partie créée, joueurs initialisées

def placerBateaux(i=0):
	# i = BateauCourant
	

	while (Partie.get_JoueurActif().get_Bateaux().get_NombreBateauxNonPlaces() > 0):

		header()
		print "===> Placer vos bateaux <====\n"
		print Partie.get_JoueurActif().get_NomJoueur()+" >> "+str(Partie.get_JoueurActif().get_Bateaux().get_NombreBateauxNonPlaces())+ " bateaux à placer."
		print "Bateau selectionné: \nTaille:"+str(Partie.get_JoueurActif().get_Bateaux().get_Bateau(i).get_taille())+"\n"
		print("Entrez une coordonnee: ")
		X = int(raw_input("X: "))
		Y = int(raw_input("Y: "))
		LastPos=Position(X,Y,Partie.get_JoueurActif().get_Bateaux().get_Bateau(i))
		try:
			Partie.get_JoueurActif().get_Grille().marquerPosition(LastPos)
			k=1
			while(k < Partie.get_JoueurActif().get_Bateaux().get_Bateau(i).get_taille()):
			
				header()
				print "===> Placer vos bateaux <====\n"
				print Partie.get_JoueurActif().get_NomJoueur()+" >> "+str(Partie.get_JoueurActif().get_Bateaux().get_NombreBateauxNonPlaces())+ " bateaux à placer."
				print "Bateau selectionné: \nTaille:"+str(Partie.get_JoueurActif().get_Bateaux().get_Bateau(i).get_taille())+"\n"
				print("Entrez une coordonnee: ")
				X = int(raw_input("X: "))
				Y = int(raw_input("Y: "))
				pos=Position(X,Y,Partie.get_JoueurActif().get_Bateaux().get_Bateau(i))
				if (pos.est_AdjacenteY(LastPos) or pos.est_AdjacenteX(LastPos)):
					try:
						Partie.get_JoueurActif().get_Grille().marquerPosition(pos)
						k = k+1

						LastPos = pos
					except:
						raw_input("Case occuppée et/ou hors grille !")
				else:
					raw_input("Mauvaise case, non adjacente.")
			# k == taille(Bateau)
			Partie.get_JoueurActif().get_Bateaux().get_Bateau(i).set_estPlace()
			i=i+1
			raw_input("Bateau place, Bateau suivant")
		except:
			raw_input("Case occuppée et/ou hors grille !")
			placerBateaux(i)
		


def demandeTir():
	header()
	print Partie.get_JoueurActif().get_NomJoueur()+" >> TIR : "
	X = int(raw_input("X: "))
	Y = int(raw_input("Y: "))
	PosTir = Position(X,Y)
	Resultat(PosTir,Partie.get_nextJoueur().get_Grille())
	raw_input("Joueur suivant")

def afficherGagnant():
	header()
	print "===================================\n"
	print "==         FIN DE PARTIE         ==\n"
	print "===================================\n"
	print "+GAGNANT: "+Partie.get_nextJoueur().get_NomJoueur()+"\n\n"
	print "-Dommage "+Partie.get_JoueurActif().get_NomJoueur()+", vous avez perdu !\n\n"
	print "===> Merci d'avoir joué ! ;)\n"
	raw_input("'Entrée' pour quitter.")
try:
	Partie = Partie()
	print "Création d'une partie à 2 joueurs"
except:
	print "Erreur lors de la création de la partie !"
demandeNoms()
# Joueur 1 Actif : Placement des bateaux
placerBateaux()
raw_input("Joueur suivant")
Partie.joueurSuivant()
# Joueur 2 Actif : Placement des bateaux 
placerBateaux()
raw_input("Joueur suivant")
Partie.joueurSuivant()

# Tous les bateaux sont placés !

# Tirs 

# TO BE CONTINUED
while (not(Partie.get_JoueurActif().a_perdu())):
	demandeTir()
	Partie.joueurSuivant()
afficherGagnant()





