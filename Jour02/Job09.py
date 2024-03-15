# Écrire un programme qui supprime les doublons de la liste suivante :
# [10,20,30,20,10,50,60,40,80,50,40].

def Double_Eraser():
    L1 = [10 , 20 , 30 , 20 , 10 , 50 , 60 , 40 , 80 , 50 , 40]
    L2 = []
    counter = 0
    
    for i in range (11):
        found = False
        for j in range(counter):
            if L1[i] == L2[j]:
                found = True
                break
        if not found:
            L2.append(L1[i])
            counter += 1
    print(L1)
    print(L2)

Double_Eraser()