# Écrire un programme qui arrondi les nombres de la liste [22.4, 4.0, 16.22, 9.10,
# 11.00, 12.22, 14.20, 5.20, 17.50].
# Puis retourner la liste dans l’ordre croissant.

def Number_Sorter():
    L1 = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

    #to round values inside the list
    for i in range (9):
        L1[i] = int(L1[i])
    print("Unsorted list: " + str(L1))

    #to sort the elements of the list
    for i in range (9):
        for j in range (0 , 8 - i):
            if L1[j] > L1[j+1]:
                L1[j], L1[j+1] = L1 [j+1] , L1[j]
    print("Sorted list: " + str(L1))


Number_Sorter()
        
