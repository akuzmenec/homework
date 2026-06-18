#1
n = input("выберите фигуру:")

if n == "а":
    for i in range(4, 0, -1):
        for g in range(i):
            print(" ", end=" ")
        for j in range(4-i):
            print("*", end=" ")
        print()

elif n == "б":
    for i in range(4):
        for g in range(i):
            print("*", end=" ")
        print()

elif n == "в":
    for i in range(4, 0, -1):
        for j in range(4-i):
            print(" ", end="")
        for g in range(i):
            print("* ", end="")
        print()

elif n == "г":
    for i in range(1, 4+1):
        for j in range(4-i):
            print(" ", end="")
        for g in range(i):
            print("* ", end="")
        print()

elif n == "д":
    for i in range(4, 0, -1):
        for j in range(4 - i):
            print(" ", end="")
        for g in range(i):
            print("* ", end="")
        print()

    for i in range(1, 4 + 1):
        for j in range(4 - i):
            print(" ", end="")
        for g in range(i):
            print("* ", end="")
        print()


elif n == "ж":

    for i in range(5):
        for g in range(i):
            print("* ", end="")
        print()

    for i in range(4-1, 0, -1):
        for g in range(i):
            print("* ", end="")
        print()


elif n == "з":


    for i in range(1, 4+1):
        for g in range(2*(4-i)):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

    for i in range(4-1, 0, -1):
        for g in range(2*(4-i)):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

elif n == "е":

    for i in range(1,4+1):
        for j in range(i):
            print("* ", end="")
        for j in range(4*(4-i)):
            print(" ", end="")
        for j in range(i):
            print("* ", end="")
        print()

    for i in range(4-1, 0, -1):
        for j in range(i):
            print("* ", end="")
        for g in range(4 * (4 - i)):
            print(" ", end="")
        for j in range(i):
            print("* ", end="")
        print()

elif n == "и":
    for i in range(4, 0, -1):
        for g in range(i):
            print("*", end=" ")
        print()

elif n == "к":
    for i in range(5):
        for g in range(i):
            print(" ", end=" ")
        for j in range(4 - i):
            print("*", end=" ")
        print()
