# À partir de la chaîne "abcdefghijklmnopqrstuvwxyz" * 10, écrire un
# programme qui récupère et affiche autant de caractères que possible de cette chaîne sous
# forme de suite pyramidale.

chain = "abcdefghijklmnopqrstuvwxyz" 
 
for index in range(len(chain)):
    print(chain[:index])
