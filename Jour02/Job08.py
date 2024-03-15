# Écrire un programme qui crée une liste nommée “L” d’au moins 5 entiers puis successivement :

# ➔ Afficher la deuxième valeur de la liste
# ➔ Écrire une fonction qui remplace L[3] par la somme des cases voisines
# L[2] & L[4], puis afficher à nouveau le tableau.
# ➔ Afficher la dernière valeur de la liste.

def listSorter ():
    L = [ 1 , 2 , 3 , 4 , 5 ]
    print(L)
    print(L[1])
    L[3] = L[2] + L[4]
    print(L)
    print(L[len(L)-1])

listSorter()