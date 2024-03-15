# Créer un programme permettant la gestion d’un inventaire.
# Créer des variables représentant un produit (nom, prix unitaire, quantité en
# stock). Afficher en console les informations du produit de manière formatée.
# Ajouter des produits en stock. Demander à l’utilisateur de saisir la quantité
# de produits qu’il souhaite acheter et mettre le stock à jour.
# Le prix produit a subi l’inflation et a augmenté de 10%, mettre à jour la
# variable correspondante.
# Afficher à nouveau toutes les informations sur le produit.

name = "Red Bull Energy Drink"
price = 2
stock = 20

print( name + " costs " + str(price) + " Euros." + " Stock remaining is " + str(20))
num = int(input("How many Drinks do you want to buy? "))

#stock change
stock = 20 - num
#price change
price += price * 0.1

print(name + " costs " + str(price) + " Euros." + " Stock remaining is " + str(stock))
