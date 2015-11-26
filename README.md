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
- get_taille  ::  Bateau -> Int
- get_estPlace  ::  Bateau -> BOOLEAN
- get_nbCasesIntactes  ::  Bateau -> Int
<br><b>+</b> Setters<br>
- set_taille  ::  Bateau x Int -> Bateau
- set_estPlace  ::  Bateau -> Bateau

<b>+</b>Enlever une case intacte au bateau<br>
- caseTouche ::  Bateau -> Bateau
Retire une case intacte du bateau

- estCoule :: Bateau -> BOOLEAN
(1) estCoule <=> nbCasesIntactes == 0 et estPlace


EnsBateaux
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- tableauBateau : List

<br>
<h4>Fonctions:</h4>
<br><b>+</b> Getters<br>
- get_Bateau  ::  EnsBateaux x Int-> Bateau
Renvoie le n-ieme bateau (A partir de 0)
- get_Premier_Bateau  ::  Bateau -> Bateau
Renvoie le bateau numero 0
- get_NombreBateauxPlaces  ::  EnsBateaux -> Int
Renvoie le nombre de bateaux placés
- get_NombreBateauxNonPlaces  ::  EnsBateaux -> Int
Renvoie le nombre de bateaux non placés
- get_NombreBateauxCoules  ::  EnsBateaux -> Int
Renvoie le nombre de bateaux coulés



<b>+</b>Ajouter/Supprimer un bateau<br>
- addBateau :: EnsBateaux x Bateau -> EnsBateaux
Ajoute un bateau à l'ensemble
- retirerBateau :: EnsBateaux x Bateau -> EnsBateaux
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
- coordonneeValide :: Grille x Position -> Boolean
- marquerPosition :: Grille x Position -> Grille
(1) marquerPosition <=> coordonneeValide
(2) marquerPosition <=> non(aUnBateau)
Ajoute la position à l'ensemble des positions occupées
- aUnBateau :: Grille x Position -> Boolean
(3) aUnBateau => coordonneeValide
Renvoie True si la position est occupée par un bateau
- estIntacte :: Grille x Position -> Boolean
(4) estIntacte <=> aUnBateau
Renvoie True si la position est occupée par un bateau et n'a pas été touchée
- quelBateau :: Grille x Position -> Bateau
(5) aUnBateau <=> quelBateau
Renvoie le bateau qui occupe la position précisé
- enleverPosition :: Grille x Position -> Grille
(6) enleverPosition <=> aUnBateau
Enleve une position des position occupées de la grille
- bateauEnVue :: Grille x Position -> Boolean
(7) Renvoie True si une case de bateau est sur la même ligne/colonne



Joueur
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- grille : Grille
- BateauxNonPlaces : Int
- BateauxPlaces : Int
- BateauxNonCoules : Int
- NomJoueur : String
- Bateaux : EnsBateaux


<br>
<h4>Fonctions:</h4>
<br><b>+</b> Getters<br>
- get_Bateaux  ::  Joueur -> EnsBateaux
- get_NomJoueur :: Joueur -> String
- get_BateauxNonPlaces :: Joueur -> Int
Renvoie le nombre de bateaux non places
- get_BateauxPlaces :: Joueur -> Int
Renvoie le nombre de bateaux places
- get_BateauxNonCoules :: Joueur -> Int
Renvoie le nombre de bateaux non coulés
- get_Grille :: Joueur -> Grille

<br><b>+</b> Setters<br>
- set_NomJoueur  ::  Joueur x String -> Joueur
 

- initBateaux :: Joueur -> EnsBateaux
Initialise un set de 5 Bateaux pour le joueur

- a_perdu :: Joueur -> Boolean
Renvoie True si le joueur a perdu


Partie
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- joueur1 : Joueur
- joueur2 : Joueur
- premierJoueur : Joueur
- deuxiemeJoueur : Joueur
- joueurActif : Joueur
- tour : INTEGER


<br>
<h4>Fonctions:</h4>
<br><b>+</b> Getters<br>
- get_joueur1  ::  Joueur -> Joueur
- get_joueur2  ::  Joueur -> Joueur
- get_JoueurActif  ::  Joueur -> Joueur
- get_nextJoueur   :: Joueur -> Joueur

<br><b>+</b> Setters<br>
- set_PremierJoueur  ::  Joueur x Joueur -> Joueur

<b>+</b>Définir le joueur jouant lors du tour n<br>
- joueurSuivant   :: Joueur x tour -> Joueur
Renvoie le joueur suivant en fonction du numero du tour et du premier joueur

Resultat
-------------
<b>Object</b><br>
<h4>Structure de données:</h4>
- Position : Position
- GrilleAdverse : GrilleAdverse
- resultat : Resultat


<br>
<h4>Fonctions:</h4>

- resultat   :: Resultat -> Fonctions
<b>+</b>Gére le message de resultat de tir à afficher à l'utilisateur<br>
- creerLoupe  :: Resultat -> String
<b>+</b>Affiche le message Loupé<br>
- creerTouche  :: Resultat -> String
<b>+</b>Affiche le message touché<br>
- creerCoule  :: Resultat -> String
<b>+</b>Affiche le message coulé<br>
- creerEnVue  :: Resultat -> String
<b>+</b>Affiche le message en Vue<br>
