# Créer un programme qui demande à l’utilisateur de renseigner son prénom
# via l’invite de commande grâce à la fonction input(). Le programme doit
# alors afficher dans la console “Hello xx !” ou xx est le prénom entré par
# l’utilisateur.

def Name():
    name = input("What's your name? ")
    print("Hello " + name)

Name()