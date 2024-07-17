import random


def dice_roll(faces):
    return random.randint(1, faces)


while True:
    try:
        n_faces = int(input("How many faces on the die? "))
        break
    except ValueError as e:
        print("You did not input a valid number")


print(f"{dice_roll(n_faces)} was rolled")
