"""
******************************************** Section #1 -> ENTÊTE ****************************************************
En vous aidant du programme fait avec l'enseignant dans le Démo1, vous devrez résoudre les probèmes proposés en
en utilisant l'instruction conditionnelle 'if' avec les principaux opérateurs de comparaison:  ==  >  <  >=  <=  != 
Vous aurez également besoin des opérateurs logiques 'and' / 'or', bien lire et comprendre les consignes avant de commencer.
**********************************************************************************************************************
"""


# ****************************** Section #2 -> Importation des modules/librairies *************************************
import os


# *************************** Section #3 -> Définition et implémentation des fonctions ********************************

def ConvertirNoteLettre():
    # Dans cette fonction vous avez à convertir une note saisie en nombre par l'utilisateur en LETTRE.
    # Ensuite avec une série de IF vous devez afficher la lettre correspondante à la note lues selon ces consignes : 
    #   0 à 59 : E     60 à 69 : D     70 à 79 : C     80 à 89 : B     90 et 100 : A
    # Ici les print() doivent être dans vos 'if' et l'affichage s'ajusté en fonction de la note saisie.
    # Vous devez afficher un message d'erreur si la note saisie est n'est pas entre 0 et 100 inclusivement.
    note = int(input("Entrez la note de l'étudiant (entre 0 et 100, sans décimale) : "))
    if note <= 59 and note >= 0:
        print("La note est F, L'étudiant n'a pas la note de passage")
    if note >= 60 and note <= 70:
        print("La note est donc un C")
    if note >= 71 and note <= 80:
        print("La note est donc un B")
    if note >= 81 and note <= 90:
        print("La note est donc un C")
    if note >= 91 and note <= 100:
        print("La note est donc un A+")
    elif note <0 or note > 100:
        print("la note n'est pas valide")



def LocaliserPlusGrandNombre():
    # On dedande à l'utilisateur d'entrer trois nombres entiers pour ensuite localiser le plus grand.
    #   - Si l'utilisateur entre 20, 8 et 12, le programme affichera : Le plus grand nombre est : 20
    #   - Si l'utilisateur entre 20, 24 et 24, le programme affichera : Le plus grand nombre est : 24
    #   - Si l'utilisateur entre 8, 8 et 8, le programme affichera : Le plus grand nombre est : 8
    # Il faut faire UN SEUL PRINT donc créer une variable nommée 'plusGrand' et votre série de 'if'
    # va servir seulement à fixer cette valeur pour un affichage après.
    nb1 = int(input("Entrez le premier nombre : "))
    nb2 = int(input("Entrez le deuxième nombre : "))
    nb3 = int(input("Entrez le troisième nombre : "))

    if nb1 >= nb2 and nb1 >= nb3 :
        plusGrand = nb1
    if nb2 >= nb1 and nb2 >= nb3 :
        plusGrand = nb2
    if nb3 >= nb1 and nb3 >= nb2 : 
        plusGrand = nb3
    print("le nombre le plus grand est : " + str(plusGrand))


def CalculerMontantGolf():
    # Cette fonction va afficher le prix d’une inscription à un club de golf en fonction de l’âge mais contrairement au démo il y a deux
    # deux éléments à tenir compte :  l'âge et le genre car en général les hommes ont tendance à jouer plus de partie dans un été.
    #   - 17 ans et moins : 250$ pour tout le monde, pour les jeunes c'est le même prix pour les garçons et les filles
    #   - 18 à 25 ans  -  homme : 450$    femme :  375$
    #   - 26 à 55 ans  -  homme : 750$    femme :  650$
    #   - 56 ans et plus  -  homme : 600$     femme : 500$
    # Attention la première valeur lue est un entier (int) et la deuxième une chaine (string), donc dans vos compairaisons vous utiliserez le 
    # double-guillemet " " quand viendra le temps de faire la vérification du genre.
    age = int(input("Entrez l'âge : "))
    sexe = input("Entrez le genre ('h' pour homme et 'f' pour femme) : ")
    if age <= 17 and age >=6 :
        print("Le prix est de 250$")
    if age <= 5:
        print("GRATUIT")
    if age >= 18 and age <= 25 and sexe == "h":
        print("Le prix est de 450$")
    if age >= 18 and age <= 25 and sexe == "f":
        print("Le prix est de 375$")
    if age >= 26 and age <= 55 and sexe == "h":
        print("Le prix est de 750$")
    if age >= 26 and age <= 55 and sexe == "f":
        print("Le prix est de 650$")
    if age >= 56 and sexe == "h":
        print("Le prix est de 600$")
    if age >= 56 and sexe == "f":
        print("Le prix est de 500$")


def ComparerSommePlusPetits():
    # Ce programme vérifie si la somme des deux plus petits nombres est inférieure, supérieure ou égale au plus grand nombre.
    #   - Si on entre 15, 9, 8 le programme affichera : La somme des deux plus petits nombres est SUPÉRIEUR au plus grand nombre.
    #   - Si on entre 2, 5 et 12 le programme affichera : La somme des deux plus petits nombres est INFÉRIEUR au plus grand.  
    #   - Si on entre 4, 5 et 9 le programme affichera : La somme des deux plus petits nombres est ÉGALE au plus grand. 
    #
    # Décomposer le problème vous devez bien analyser la problématique car initialement votre tâche consistera à localiser
    # le plus grand nombre, c'est important que le programme fonctionne peu importe l'endroit ou il est entré.  Donc au départ
    # localisez le plus grand nombre et placez le dans nb1 ou nb3 c'est à vous de voir.
    # Ensuite lorsque vous saurez ou est situé le plus grand nombre vous pourrez faire la comparaison demandée.
    nb1 = int(input("Entrez le premier nombre : "))
    nb2 = int(input("Entrez le deuxième nombre : "))
    nb3 = int(input("Entrez le troisième nombre : "))
    
    
    if nb1 >= nb2 and nb1 >= nb3 :
        plusGrand = nb1
        somme = nb2 + nb3
    if nb2 >= nb1 and nb2 >= nb3 :
        plusGrand = nb2
        somme = nb1 + nb3
    if nb3 >= nb1 and nb3 >= nb2 : 
        plusGrand = nb3
        somme = nb1 + nb2

    if plusGrand > somme:
        print("La somme des deux plus petits nombres est INFÉRIEUR au plus grand. ")
    if plusGrand == somme:
        print("La somme des deux plus petits nombres est ÉGALE au plus grand. ")
    if plusGrand < somme:
        print("La somme des deux plus petits nombres est SUPÉRIEUR au plus grand. ")


def DeterminerTypeTriangle():
    # Cette fonction sert à déterminer si un triangle est considéré à angle droit (avec un angle de 90 degré),  
    # à angle obtus (avec un angle supérieur à 90) ou à angle aigu (tous les angles sont inférieurs à 90).
    #   - Exemple #1 : 90  60  30  -->  Triangle rectangle (à angle droit)
    #   - Exemple #2 : 65  40  75  -->  Triangle à angle aigu
    angle1 = int(input("Entrez le premier angle : "))
    angle2 = int(input("Entrez le deuxième angle : "))
    angle3 = int(input("Entrez le troisième angle : "))
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Ce triangle possède un angle droit")
    if angle1 < 90 and angle2 < 90 and angle3 < 90 :
        print("Ce triangle est aigus")
    if angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Ce triangle est obtus")
    



# ******************************************* Section #4 -> Corps du programme ********************************************************
os.system("cls")
print("1- Déterminer la lettre correspondante à une note située entre 0 et 100")
print("2- Localiser le plus grand nombre parmis les trois saisis")
print("3- Afficher le montant à payer pour une inscription au club de golf")
print("4- Comparer la somme des deux plus petits nombres avec le plus grand")
print("5- Déterminer le type de triangle en fonction des trois angles")
reponse = int(input("Entrez votre réponse et appuyez sur Entrée (Enter) : "))   
if reponse == 1:
    ConvertirNoteLettre()
if reponse == 2:
    LocaliserPlusGrandNombre()
if reponse == 3:
    CalculerMontantGolf()
if reponse == 4:
    ComparerSommePlusPetits()
if reponse == 5:
    DeterminerTypeTriangle()