# -*- coding: utf-8 -*-

class Position:
	def __init__(self,X,Y,Bateau=None,Tire=False):
		self.X=X
		self.Y=Y
		self.Bateau=Bateau
		self.Tire = Tire

#### GETTERS ####
	def getX(self):
		return self.X
	def getY(self):
		return self.Y
	def get_Tire(self):
		return self.Tire
	def set_Tire(self):
		self.Tire=True
	def getBateau(self):
		return self.Bateau
		
	def placerBateau(self,Grille,Bateau):
	# Position x Grille x Bateau -> Grille
	# placerBateau(self,Joueur) <=> Joueur.Grille.coordonneValide(self)
		if (Grille.coordonneValide(self)):
			if not(Grille.aUnBateau(self)):
				Grille.marquerPosition(self)

	def est_AdjacenteX(self,Position):
		return (Position.getX() == self.getX()+1 or Position.getX() == self.getX()-1)

	def est_AdjacenteY(self,Position):
		return (Position.getY() == self.getY()+1 or Position.getY() == self.getY()-1)









