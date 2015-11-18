# -*- coding: utf-8 -*-
class Resultat:
	def __init__(self,Position,GrilleAdverse):
		self.Position = Position
		self.GrilleAdverse = GrilleAdverse
		self.resultat()

	def resultat(self):
		if (self.GrilleAdverse.estIntacte(self.Position)):
			
			self.GrilleAdverse.enleverPosition(self.Position)	
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
		return "\n\nLoupé !\n"

	def creerCoule(self):
		Bateau = self.GrilleAdverse.quelBateau(self.Position)
		Bateau.caseTouche()	# On enlève une case du tableau	
		return "\n\nCoulé !\n"

	def creerEnVue(self):
		
		return "\n\nEn Vue !\n"

	def creerTouche(self):
		Bateau = self.GrilleAdverse.quelBateau(self.Position)
		Bateau.caseTouche() # On enlève une case du tableau
		return "\n\nTouche !\n"