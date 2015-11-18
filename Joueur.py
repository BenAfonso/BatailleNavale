# -*- coding: utf-8 -*-
from Grille import Grille
from Bateau import Bateau
from EnsBateaux import EnsBateaux
class Joueur:
	def __init__(self):
		self.Grille = Grille()
		self.BateauxNonPlaces = 0
		self.BateauxPlaces = 0
		self.BateauxNonCoules = 0
		self.NomJoueur = ""
		self.Bateaux = EnsBateaux()
		self.initBateaux()

	def get_Bateaux(self):
		return self.Bateaux

	def initBateaux(self):
		self.Bateaux.add_Bateau(Bateau(1))
		self.Bateaux.add_Bateau(Bateau(2))
		#self.Bateaux.add_Bateau(Bateau(3))
		#self.Bateaux.add_Bateau(Bateau(4))
		#self.Bateaux.add_Bateau(Bateau(5))

	def get_NomJoueur(self):
		return self.NomJoueur
	def get_BateauxNonPlaces(self):
		return self.BateauxNonPlaces
	def get_BateauxPlaces(self):
		return self.BateauxPlaces
	def set_NomJoueur(self,NomJoueur):
		self.NomJoueur = NomJoueur

	def get_Grille(self):
		return self.Grille

	def a_perdu(self):
		return self.Bateaux.get_NombreBateauxCoules() == self.Bateaux.get_NombreBateauxPlaces()



	def placerBateau(self,n,Position):
		'''Place le bateau n'''
		# Precondition : 0 <= n <= len(BateauxNonPlaces)

		# Retirer bateau liste bateaux nons placés

		self.BateauxPlaces = self.BateauxPlaces + 1

