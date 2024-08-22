"""
******************************************** Section #1 -> ENTÊTE ****************************************************
Ce projet sert à explorer différentes utilisations de l'instruction conditionnelle 'if' avec les principaux opérateurs
de comparaison courramment utilisés:    ==   >   <   >=   <=   != 
On y retrouve également des exemples d'utilisation du 'if' avec les opérateurs logiques 'and' / 'or'
**********************************************************************************************************************
"""


# ****************************** Section #2 -> Importation des modules/librairies *************************************
# Ce module permet l'utilisation de plusieurs fonctions mathématiques, dans ce projet on va utiliser la fonction .pow()
import math
# Ce module permet l'utilisation de différentesfonctions associés au système d'exploitation (operating system),
# dans ce projet nous allons utiliser le os.system("cls") qui sert à VIDER L'ÉCRAN console (voir plus bas).
import os


# *************************** Section #3 -> Définition et implémentation des fonctions ********************************

def DeterminerCategorieSoccer():
    # Pour vérifier si deux valeur sont égales dans un IF, il faut utiliser le '==' car le '=' sert à L'AFFECTATION.
    anneeNaissance = int(input("Entrez l'année de naissance de l'athlète : "))
    if anneeNaissance == 2010: 
        print("La catérogie est U12")
    if anneeNaissance == 2011: 
        print("La catégorie est U11")
    # A compléter...

def DeterminerCategorieHockey():
    # Avec l'opérateur 'or' ça prend UNE SEULE CONDITION DE VRAIE dans le lot pour que l'ensemble du IF soit vrai
    age = int(input("Entrez l'âge de l'athlète : "))
    if age == 13 or age == 14:
        print("La catégorie est bantam")
    if age == 11 or age == 12:
        print("La catégorie est pee wee")
    if age == 9 or age == 10:
        print("La catégorie est atome")
    if age == 7 or age == 8:
        print("La catégorie est novice")
    # A compléter...

def CalculerMontantGolf():
    # Avec l'opérateur 'and' TOUTES LES CONDITIONS DOIVENT ÊTRE VRAIES pour que l'ensemble du IF soit considéré vrai
    age = int(input("Entrez l'âge de l'athlète : "))
    if age < 5:
        montant = 0
    if age >= 5 and age <= 17:  # Imaginez ce IF avec des 'or' ça en prendrait beaucoup trop, pas optimal du tout!
        montant = 250
    if age >= 18 and age <= 25:
        montant = 450
    # A compléter...

    # Remarquez bien ici que le print() n'est pas dans la série de IF, je ne fais que fixer le montant pour l'affiché à la fin.
    print("Le montant à payer pour ce jouer ou cette joueuse est: " + str(montant) + "$")

def ComparerCarre():
    # Dans cette fonction nous allons demander à l'utilisateur d'entrez deux NOMBRES ENTIERS, le but est de calculer le carré 
    # du PLUS PETIT nombre et de le comparer au PLUS GRAND nombre (affiché s'il est plus grand, plus petit ou égal).
    x = int(input("Entrez un premier nombre : "))
    y = int(input("Entrez un deuxième nombre : "))   
    # Au départ on veut s'assurer que la plus petite valeur soit stocker dans la variable 'x'
    # Donc on va vérifier si y est plus petit que x, si c'est le cas on inverse les deux valeurs.
    # Nous n'avons pas besoin de vérifier si x est plus petit que y car si c'est le cas les valeurs sont bien placées.
    if y < x:
        x, y = y, x     # En Python cette affectation permet d'inverser deux variables, x devient y et y devient x
    
    # Après le IF précédent, nous sommes certain à 100% que le plus petit nombre sera toujours situé dans 'x'
    # Donc à partir de là on peut calculer le carré du plus petit nombre (x) et le comparé avec le plus grand (y)
    carre = math.pow(x, 2)      # La fonction .pow() met à la puissance le nombre, donc à la puissance 2 c'est le carré.
    if carre > y:
        print("Le carré de " + str(x) + " est " + str(carre) + " donc PLUS GRAND que le 2e nombre qui est : " + str(y))
    if carre < y:
        print("Le carré de " + str(x) + " est " + str(carre) + " donc PLUS PETIT que 2e nombre qui est : " + str(y))
    if carre == y:
        print("Le carré de " + str(x) + " est " + str(carre) + " donc ÉGAL au 2e nombre qui est : " + str(y))


# ******************************************* Section #4 -> Corps du programme ********************************************************
os.system("cls")    # Sert à VIDER l'écran console avant l'affichage de notre menu (disponible car la librairie a été importée en haut).
# Dans ce projet, nous affichons initialement toutes les options disponibles pour l'utilisateur.
print("1- Déterminer la catégorie lors de l'inscription au soccer, en fonction de l'année de naissance")
print("2- Déterminer la catégorie lors de l'inscription au hockey mineur, en fonction de l'âge")
print("3- Calculer le montant à payer pour une inscription au club de golf, en fonction de l'âge")
print("4- Comparer le CARRÉ du plus petit nombre avec le plus grand nombre")
reponse = int(input("Entrez votre réponse et appuyez sur Entrée (Enter) : "))     
if reponse == 1:
    DeterminerCategorieSoccer()
if reponse == 2:
    DeterminerCategorieHockey()
if reponse == 3:
    CalculerMontantGolf()
if reponse == 4:
    ComparerCarre()
if reponse != 1 and reponse != 2 and reponse != 3 and reponse != 4:
    print("Votre réponse n'est pas dans les options offertes donc aucune action ne sera faite.")