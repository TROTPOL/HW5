
from cards import Game 


def playgame():
    print(f"Привіт! Маєте бажання поворожити?")
    a = input("Введіть, 'Так', або 'Ні'")

    while True:
        if a == "Так":
            return Game.divination()
        elif a == "Ні":
            print('До зустрічі!')
            break
        else:
            a = input("Введіть 'Так', або 'Ні'")

def repeat():
        return Game.divination()

        
                
playgame()

a = None
while True:
    print(f"Маєте ще питання?")
    a = input("Введіть, 'Так', або 'Ні'")
    if a == "Так":
               repeat() 
               
    elif a == "Ні":
                print('До зустрічі!')
                break
    else:
                    a = input("Введіть 'Так', або 'Ні'")


    
