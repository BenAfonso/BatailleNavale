# Bataille Navale

Programme de Bataille Navale développé en Python.

**Version de l'interpréteur : Python 2.7**

## **Classes**

### **Bateau**

> #### **Object**
#### Structure de données
- taille : INTEGER
- estPlace : BOOLEAN
- nbCasesIntactes : INTEGER
#### Fonctions

>  **Getters**
- get_taille  ::  Bateau -> Int
- get_estPlace  ::  Bateau -> BOOLEAN
- get_nbCasesIntactes  ::  Bateau -> Int
>
 **Setters**
- set_taille  ::  Bateau x Int -> Bateau
- set_estPlace  ::  Bateau -> Bateau

>  **Enlever une case intacte au bateau**
- caseTouche ::  Bateau -> Bateau
Retire une case intacte du bateau
- estCoule :: Bateau -> BOOLEAN
>
  ***Précondition:***

>       (1) estCoule <=> nbCasesIntactes == 0 et estPlace


### **EnsBateaux**

> #### **Object**
#### Structure de données
- tableauBateau : List
#### Fonctions

>  **Getters**
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
>
 **Ajouter/Supprimer un bateau**
- addBateau :: EnsBateaux x Bateau -> EnsBateaux
Ajoute un bateau à l'ensemble
- retirerBateau :: EnsBateaux x Bateau -> EnsBateaux
Retire un bateau de l'ensemble

### **Grille**

> **Object**
#### Structure de données
- hauteur : Int
- largeur : Int
- positionsOccuppees : List
#### Fonctions

>  **Getters**
- coordonneeValide :: Grille x Position -> Boolean
- marquerPosition :: Grille x Position -> Grille
Ajoute la position à l'ensemble des positions occupées
- aUnBateau :: Grille x Position -> Boolean
Renvoie True si la position est occupée par un bateau
- estIntacte :: Grille x Position -> Boolean
Renvoie True si la position est occupée par un bateau et n'a pas été touchée
- quelBateau :: Grille x Position -> Bateau
Renvoie le bateau qui occupe la position précisé
- enleverPosition :: Grille x Position -> Grille
Enleve une position des position occupées de la grille
- bateauEnVue :: Grille x Position -> Boolean
>
 ***Précondition***

>         (1) marquerPosition <=> coordonneeValide
         (2) marquerPosition <=> non(aUnBateau)
         (3) aUnBateau => coordonneeValide
         (4) estIntacte <=> aUnBateau
         (5) aUnBateau <=> quelBateau
         (6) enleverPosition <=> aUnBateau
         (7) Renvoie True si une case de bateau est sur la même ligne/colonne


### **Joueur**

> **Object**
#### Structure de données
- grille : Grille
- BateauxNonPlaces : Int
- BateauxPlaces : Int
- BateauxNonCoules : Int
- NomJoueur : String
- Bateaux : EnsBateaux
#### Fonctions

>  **Getters**
- get_Bateaux  ::  Joueur -> EnsBateaux
- get_NomJoueur :: Joueur -> String
- get_BateauxNonPlaces :: Joueur -> Int
Renvoie le nombre de bateaux non places
- get_BateauxPlaces :: Joueur -> Int
Renvoie le nombre de bateaux places
- get_BateauxNonCoules :: Joueur -> Int
Renvoie le nombre de bateaux non coulés
- get_Grille :: Joueur -> Grille
>
  **Setters**
- set_NomJoueur  ::  Joueur x String -> Joueur
- initBateaux :: Joueur -> EnsBateaux
Initialise un set de 5 Bateaux pour le joueur
- a_perdu :: Joueur -> Boolean
Renvoie True si le joueur a perdu


### **Partie**

> **Object**
#### Structure de données
- joueur1 : Joueur
- joueur2 : Joueur
- premierJoueur : Joueur
- deuxiemeJoueur : Joueur
- joueurActif : Joueur
- tour : INTEGER
>
 #### Fonctions

>  **Getters**
- get_joueur1  ::  Joueur -> Joueur
- get_joueur2  ::  Joueur -> Joueur
- get_JoueurActif  ::  Joueur -> Joueur
- get_nextJoueur   :: Joueur -> Joueur

>  **Setters**
- set_PremierJoueur  ::  Joueur x Joueur -> Joueur

>  **Définir le joueur jouant lors du tour n**
- joueurSuivant   :: Joueur x tour -> Joueur
Renvoie le joueur suivant en fonction du numero du tour et du premier joueur

### **Resultat**

> **Object**
#### Structure de données
- Position : Position
- GrilleAdverse : GrilleAdverse
- resultat : Resultat
#### Fonctions
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

## **Démonstration**

[![asciicast](https://asciinema.org/a/904o7ktf45uhrjjcaunqalf79.png)](https://asciinema.org/a/904o7ktf45uhrjjcaunqalf79)


## **Auteurs**

AFONSO Benjamin,
BOUTHINON Alexandre
