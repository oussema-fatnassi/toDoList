# Créer un programme permettant la simulation financière pour un investissement.
# Initialiser deux variables, une pour le montant initial de l’investissement et une
# pour le taux de rendement annuel en pourcentage.
# Afficher en console le gain annuel en fonction du taux de rendement.
# L’investisseur augmente son capital de 5 000 euros, le taux augmenta de 2%.
# Calculer à nouveau le gain de l’investisseur et afficher en console le résultat.
# L'investisseur retire 10% du montant total, suite à ce retrait, le rendement diminue de 1%.
# Calculer le montant final de l’investissement et afficher le nouveau gain.

initial_investment = 20000
interest_rate = 8

gain = (initial_investment*interest_rate)/100

print ("Initial investment: " + str(initial_investment) + "\nAnnual rate of return: " + str(interest_rate) + " %" + "\nGain: " + str(gain) )
#print ("Your gain is " + str(gain) + " after an initial investment of " + str(initial_investment) + " and a annual return of " + str(interest_rate
#) + " %")

augmented_interest_rate = (interest_rate + 2)
augmented_capital = int(input("How much do you want to invest? "))
balance = (initial_investment + gain + augmented_capital)
balance += (balance * augmented_interest_rate)/100

print ("New balance: " + str(balance) + "\nAugmented annual percentage rate of return: " + str(augmented_interest_rate) + " %")
Withdraw_percentage = int(input("What percentage do you want to withdraw? "))

balance -= (balance * Withdraw_percentage)/100
interest_rate = augmented_interest_rate - 1
gain = (balance*interest_rate)/100

print("New balance: " +str(balance) + "\nNew Interest Rate: " + str(interest_rate) +"\nGain: " +str(gain) )

