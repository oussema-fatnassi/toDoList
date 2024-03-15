# Créer une fonction qui prend en paramètre un string et qui la retourne
# inverser. Par exemple, « nikana » deviendra « anakin ».

#reversed_str = ''.join(reversed('anakin'))

def Reverse(word):
    lengh = len(word)
    reversed_word = ""
    
    for i in range(-1,-lengh-1,-1):
        reversed_word += word[i]
        
    return reversed_word
   

print(Reverse(input("Give me a word to reverse ")))

