from random import *
def Flower_or_nonsense(Health1, Health2):
    print("👊🏻        👊🏻")
    i = choice(["R", "L"])
    Guess = input("Right or left? < R, L > :")
    while Guess not in ["R", "L"]:
        Guess = input("Right or left? < R, L > :")
    if Guess==i:
        if i == "L":
            print("💍        🖐🏻")
        else:
            print("🖐🏻        💍")
        Health2 -= 10
    else:
        if i == "L":
            print("💍        🖐🏻")
        else:
            print("🖐🏻        💍")
        print("☠")
        Health1 -= 10
        
Flower_or_nonsense(100, 100)
