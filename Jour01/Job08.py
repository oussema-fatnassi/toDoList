# Créer un programme qui affiche en console les tables de multiplication de 1 à N.
# N étant un entier supérieur à zéro saisi par l’utilisateur.
# N'oubliez pas de vérifier tout ce qui est nécessaire pour assurer la fiabilité de votre programme.


N = int(input("Type an integer superior to 0 (N): "))
print ("Moltiplication Table of " + str(N))


for i in range (1,11):
   print(N, 'x', i, '=', N*i)
