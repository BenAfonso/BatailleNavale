Bataille Navale<br>
-----------------------------------------
<i>Python 2.7<i><br>

# Classes

Bateau
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- taille : INTEGER
- estPlace : BOOLEAN
- nbCasesIntactes : INTEGER

<br>
<h4>Fonctions:</h4>
<br><b>+</b> Getters<br>
- get_taille(self)  ::  Bateau -> Int
- get_estPlace(self)  ::  Bateau -> BOOLEAN
- get_nbCasesIntactes(self)  ::  Bateau -> Int
<br><b>+</b> Setters<br>
- set_taille(self)  ::  Bateau x Int -> Bateau
- set_estPlace(self)  ::  Bateau -> Bateau

<b>+</b>Enlever une case intacte au bateau<br>
- caseTouche(self) ::  Bateau -> Bateau

- estCoule(self) :: Bateau -> BOOLEAN


EnsBateaux
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- tableauBateau : List

<br>
<h4>Fonctions:</h4>
<br><b>+</b> Getters<br>
- get_Bateau(self,n)  ::  EnsBateaux x Int-> Bateau
Renvoie le n-ieme bateau (A partir de 0)
- get_Premier_Bateau(self)  ::  Bateau -> Bateau
Renvoie le bateau numero 0
- get_NombreBateauxPlaces(self)  ::  EnsBateaux -> Int
Renvoie le nombre de bateaux placés
- get_NombreBateauxNonPlaces(self)  ::  EnsBateaux -> Int
Renvoie le nombre de bateaux non placés
- get_NombreBateauxCoules(self)  ::  EnsBateaux -> Int
Renvoie le nombre de bateaux coulés



<b>+</b>Ajouter/Supprimer un bateau<br>
- addBateau(self,Bateau) :: EnsBateaux x Bateau -> EnsBateaux
Ajoute un bateau à l'ensemble
- retirerBateau(self,Bateau) :: EnsBateaux x Bateau -> EnsBateaux
Retire un bateau de l'ensemble

Grille
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- hauteur : Int
- largeur : Int
- positionsOccuppees : List

<br>
<h4>Fonctions:</h4>
<br><b>+</b> Getters<br>
- coordonneeValide(self,Position) :: Grille x Position -> Boolean
- marquerPosition(self,Position) :: Grille x Position -> Grille
Ajoute la position à l'ensemble des positions occupées
- aUnBateau(self,Position) :: Grille x Position -> Boolean
Renvoie True si la position est occupée par un bateau
- estIntacte(self,Position) :: Grille x Position -> Boolean
Renvoie True si la position est occupée par un bateau et n'a pas été touchée
- quelBateau(self,Position) :: Grille x Position -> Bateau
Renvoie le bateau qui occupe la position précisé
- enleverPosition(self,Position) :: Grille x Position -> Grille
Enleve une position des position occupées de la grille
- bateauEnVue(self,Position) :: Grille x Position -> Boolean
Renvoie True si une case de bateau est sur la même ligne/colonne



Joueur
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- grille : Grille
- BateauxNonPlaces : Int
- BataeuxPlaces : Int
- BateauxNonCoules : Int
- NomJoueur : String
- Bateaux : EnsBateaux


<br>
<h4>Fonctions:</h4>
<br><b>+</b> Getters<br>
- get_Bateaux(self)  ::  Joueur -> EnsBateaux
- get_NomJoueur(self) :: Joueur -> String
- get_BateauxNonPlaces(self) :: Joueur -> Int
- get_BateauxPlaces(self) :: Joueur -> Int
- get_BateauxNonCoules(self) :: Joueur -> Int
- get_Grille(self) :: Joueur -> Grille


# TO BE CONTINUED


