# Créer une fonction qui prend en paramètre un nombre nommé “nombre”.
# Afficher “positif” si le nombre est supérieur à 0.
# Afficher “négatif” si le nombre est inférieur à 0.
# Appeler cette fonction plusieurs fois en y passant des paramètres différents
# pour afficher ces résultats.

def Positive_Negative(nombre):
    if nombre >= 0:
        return "Positive"
    else:
        return "Negative"
    
print(Positive_Negative(5))
print(Positive_Negative(0))
print(Positive_Negative(-4))
