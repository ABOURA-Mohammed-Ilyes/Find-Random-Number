import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)

def correct_number():
    nombre=0
    while not 0 < nombre < 11 :
        try:
            nombre = int(input(f"Veuillez deviner un chiffre magique entre {NOMBRE_MIN} et {NOMBRE_MAX} = "))
        except ValueError :
            print("Veuillez indiquer un chiffre correcte")
    return nombre

def check(number):
    if number == NOMBRE_MAGIQUE :
        print("Bsahtek ya sahlouf")
        return True
    elif number < NOMBRE_MAGIQUE :
        print(f"3awed a lehmar, le chiffre kbir 3la {number}")
        return False
    else :
        print(f"3awed a lehmar, le chiffre sghir 3la {number}")
        return False
    
n=5
print(f"Tu as {n} essai")
reponse = False
while reponse == False and n > 0 :
    reponse = check(correct_number())
    if not reponse : 
        n-=1
        print(f"Il te reste {n} essai")
    else :
        print("BRAVO! 3jebtni")
        break
if n == 0 : 
    print("YOU LOST LOSER !")