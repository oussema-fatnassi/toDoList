# Écrire un programme qui affiche dans la console un rectangle avec des ‘-’ et
# des ‘|’ en fonction des paramètres d’entrées, (width, height), par exemple : draw_rectangle(10, 3)

def Draw_Rectangle():
    width = 10
    height = 3
    dash = "-"
    line = "|"
    empty = " "
    
    for i in range (height+2):
        if i == 0 or i == height+1:
            print ((dash + " ")*width)
        else:
            print (line + empty*(width-1)*2 + line)

Draw_Rectangle()