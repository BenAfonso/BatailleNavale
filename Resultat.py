# -*- coding: utf-8 -*-
class Resultat:
	def __init__(self,Position,GrilleAdverse):
		self.Position = Position
		self.GrilleAdverse = GrilleAdverse
		self.resultat()

	def resultat(self):
		if (self.GrilleAdverse.aUnBateau(self.Position)):
			BateauTouche=self.GrilleAdverse.quelBateau(self.Position)
			if (BateauTouche.get_nbCasesIntactes() > 1):
				print(self.creerTouche())
			else:
				print(self.creerCoule())
		elif (self.GrilleAdverse.bateauEnVue(self.Position)):
			print(self.creerEnVue())
		else:
			print(self.creerLoupe())


	def creerLoupe(self):
		return "Loupé !"

	def creerCoule(self):
		Bateau = self.GrilleAdverse.quelBateau(self.Position)
		Bateau.set_taille(Bateau.get_nbCasesIntactes()-1) # On enlève une case du tableau		
		return "Coulé !"

	def creerEnVue(self):
		
		return "En Vue !"

	def creerTouche(self):
		Bateau = self.GrilleAdverse.quelBateau(self.Position)
		Bateau.set_taille(Bateau.get_nbCasesIntactes()-1) # On enlève une case du tableau
		return "Touche !"