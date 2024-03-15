# Créer une fonction qui prend en paramètre une String nommée “langage”.
# Si la valeur de “langage” est égale à “JavaScript” affichez “tu es un
# développeur web”
# Sinon si la valeur de “langage” est égale à “python” affichez “tu es un
# développeur IA”
# Sinon si la valeur de “langage” est égale à “java” affichez “tu es un
# développeur logiciel”
# Sinon si la valeur de “langage” est égale à “reactjs” affichez “tu es un
# développeur mobile”
# Sinon, affichez “un jour, je serai le meilleur développeur... ”

def Whats_your_spe (langage):
    if langage == "JavaScript":
        print("You are a web developper")
    elif langage == "Python":
        print("You are a AI developper")
    elif langage == "Java":
        print("You are a system developer")
    elif langage == "Reactjs":
        print ("You are a mobile developper")
    else:
        print ("One day, i will be the best developper")
    
Whats_your_spe("JavaScript")
Whats_your_spe("Python")
Whats_your_spe("Java")
Whats_your_spe("Reactjs")
Whats_your_spe("Nothing")