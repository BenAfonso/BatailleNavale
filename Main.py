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
	print "=============== BATAILLE NAVALE ===============\n"

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
		LastPos=Position(X,Y)
		Partie.get_JoueurActif().get_Grille().marquerPosition(LastPos)
		print "Bravo bon choix !"
		k=1
		while(k < Partie.get_JoueurActif().get_Bateaux().get_Bateau(i).get_taille()):
			header()
			print "===> Placer vos bateaux <====\n"
			print Partie.get_JoueurActif().get_NomJoueur()+" >> "+str(Partie.get_JoueurActif().get_Bateaux().get_NombreBateauxNonPlaces())+ " bateaux à placer."
			print "Bateau selectionné: \nTaille:"+str(Partie.get_JoueurActif().get_Bateaux().get_Bateau(i).get_taille())+"\n"
			print("Entrez une coordonnee: ")
			X = int(raw_input("X: "))
			Y = int(raw_input("Y: "))
			pos=Position(X,Y)
			if (pos.est_AdjacenteY(LastPos) or pos.est_AdjacenteX(LastPos)):
				try:
					Partie.get_JoueurActif().get_Grille().marquerPosition(pos)
					print "Bravo belle case !"
					k = k+1
					LastPos = pos
				except:
					print("Oops !")
			else:
				print "Mauvaise case, non adjacente."
		Partie.get_JoueurActif().get_Bateaux().get_Bateau(i).set_estPlace()
		i=i+1





try:
	Partie = Partie()
	print "Création d'une partie à 2 joueurs"
except:
	print "Erreur lors de la création de la partie !"
demandeNoms()
# Joueur 1 Actif : Placement des bateaux
placerBateaux()
Partie.joueurSuivant()
# Joueur 2 Actif : Placement des bateaux 
placerBateaux()
Partie.joueurSuivant()

# Tous les bateaux sont placés !

# Tirs
i=0 
while (i<10):
	i=i+1
	header()
	print Partie.get_JoueurActif().get_NomJoueur()+" >> TIR : "
	X = int(raw_input("X: "))
	Y = int(raw_input("Y: "))
	PosTir = Position(X,Y)
	Resultat(PosTir,Partie.get_JoueurSuivant().get_Grille())
	raw_input("Nouveau Tir")






