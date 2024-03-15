#a = float(input("Type an integer bigger than 0: "))
#b = float(input("Type an integer bigger than 0: "))
#c = float(input("Type an integer bigger than 0: "))
import math

a=3
b=1
c= math.sqrt(2)

if a+b>=c and b+c>=a and a+c>=b:
    if a==b==c:
        print("The triangle is equilateral")

    elif a==b or b==c or c==a:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 +c**2 == b**2:
            print("The triangle is isoscele and rectangle")
        else: 
            print("The triangle is isoscele")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 +c**2 == b**2:
            print("The triangle is rectangle")
    else:
        print("The triangle is scalene")
else:
    print("The three numbers can't constitute a triangle")
