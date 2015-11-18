# -*- coding: utf-8 -*-
class EnsBateaux:

	def __init__(self):
		self.tableauBateau = []

	def get_Bateau(self,n):
	# Récupère le n-ième bateau
		return self.tableauBateau[n]

	def get_Premier_Bateau(self):
		return self.get_Bateau(0)

	def add_Bateau(self,Bateau):
		# EnsBateau x Bateau -> EnsBateaux
		self.tableauBateau.append(Bateau)

	def retirerBateau(self,n):
		# EnsBateau x Bateau -> EnsBateau ?????
		for i in range (n,len(self.tableauBateau)-1):
			self.tableauBateau[i] = self.tableauBateau[i+1]
			# On bouge tout

	def get_NombreBateauxPlaces(self):
		cpt=0
		for Bateau in self.tableauBateau:
			if Bateau.estPlace:
				cpt = cpt+1
		return cpt
		
	def get_NombreBateauxNonPlaces(self):
		cpt=0
		for Bateau in self.tableauBateau:
			if not(Bateau.estPlace):
				cpt = cpt+1
		return cpt

	def get_NombreBateaux(self):
		cpt=0
		for Bateau in self.tableauBateau:
			cpt = cpt+1
		return cpt
