# Créer une fonction nommée “my_sort” qui compare les éléments d’une liste
# et échange de place uniquement avec l’élément de la liste adjacent jusqu'à
# que la liste soit entièrement triée dans l’ordre croissant. La fonction doit
# retourner la liste triée et afficher le nombre total de coups nécessaire pour
# trier cette liste.
# Pensez à commenter chaque étape de votre logique.

def my_sort(list):

    lengh = len(list)
    counter = 0

    for i in range (lengh):
        for j in range (0 , lengh - i - 1):
            if list[j] > list[j+1]:

                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                counter += 1

                #prints all the iteration to sort the list
                print(list)

    print("Sorted list: " + str(list))
    print("Total number of itarations to sort the list: " + str(counter))

L1 = [ 15, 27, 2 , 36 , 1 , 66 , 78 , 3]
my_sort(L1)