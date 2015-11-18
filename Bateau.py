# -*- coding: utf-8 -*-
class Bateau:
	def __init__(self,taille,estPlace=False):
		self.taille = taille
		self.estPlace = estPlace
		self.nbCasesIntactes = taille

	def get_estPlace(self):
		return self.estPlace

	def get_nbCasesIntactes(self):
		return self.nbCasesIntactes

	def caseTouche(self):
		self.nbCasesIntactes = self.nbCasesIntactes - 1

	def set_estPlace(self):
		self.estPlace = True


	def get_taille(self):
		return self.taille

	def set_taille(self,taille):
		self.taille = taille

	def estCoule(self):
		return (self.nbCasesIntactes == 0)

