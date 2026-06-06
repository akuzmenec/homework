###HOMEWORK_1
from unicodedata import category


def homework_1():
    # 1
    a = int(input())
    b = int(input())
    c = int(input())

    sum = a + b + c
    prod = a * b * c

    print(f"sum = {sum}, product = {prod}")

    #2

    sal = int(input("salary:"))
    cred = int(input("credit:"))
    ar = int(input("arrears:"))

    result = sal - cred - ar

    print(result)

    #3
    d_1 = int(input())
    d_2 = int(input())

    s = (d_1 + d_2)/2

    print(s)

    #4

    print("To be \nor not \nto be")

    #4

    print("Life is what happenes \n when \n  you're buse making other plans")

###HOMEWORK_2
def homework_2():

    type_ = input("Введите тип учебного  материала (книга/видео):")
    cost = int(input("Введите стоимость материала:"))
    category = input("Введите категорию материала:")

    if cost > 0:
        print(f"Материал добавлен: Тип - {type_}, Стоимость - {cost}, Категория - {category}")
    else:
        print("Error: цена указана неверно")

###HOMEWORK_3
def homework_3():

    #1

    age = int(input())

    if (age > 0) and (age <= 12):
        print("ребенок")

    elif (age > 12) and (age <= 18):
        print("подросток")

    elif (age > 18) and (age <= 60):
        print("взрослый")

    elif age > 60:
        print("пенсионер")

    else:
        print("неправильно введен возраст")


    #2

    a = int(input("Введите число от 0 до 9:"))
    if a == 0:
        print("0-)")
    elif a == 1:
        print("1-!")
    elif a == 2:
        print("2-@")
    elif a == 3:
        print("3-#")
    elif a == 4:
        print("4-$")
    elif a == 5:
        print("5-%")
    elif a == 6:
        print("6-^")
    elif a == 7:
        print("7-&")
    elif a == 8:
        print("8-*")
    elif a == 9:
        print("9-(")
    else:
        print("Error: неправильно введено число")

    #3

    b = int(input("введите 3-x значное число:"))

    b_3 = b%10
    b_1 = b//100
    b_2 = (b//10)%10
    if ((b_3 == b_1) or (b_3 == b_2)) or ((b_1 == b_2) or (b_1 == b_3)) or ((b_2 == b_1) or (b_2 == b_3)):
        print("Yes")
    else:
        print("No")

    #4
    year = int(input("введите год"))

    if (((year % 400) == 0) or ((year % 4) == 0)) and year % 100 != 0:
        print("yes")
    else:
        print("no")

    #5

homework_3()

