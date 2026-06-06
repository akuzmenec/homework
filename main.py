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

    num = int(input("введите пятизначное число:"))

    c_1 = num//10000
    c_2 = (num//1000)%10
    c_3 = (num//100)%10
    c_4 = (num//10)%10
    c_5 = num%10

    if str(num) == f"{c_5}{c_4}{c_3}{c_2}{c_1}":
        print("yes")

    else:
        print("no")

    #6

    v = input("выберите валюту (EUR,UAN,AZN):")
    s = float(input("ведите сумму:"))
    if v == "EUR" or "eur":
        print(1.165 * s)
    elif v == "UAN" or "uan":
        print(0.02 * s)
    elif v == "AZN" or "azn":
        print(0.5882 * s)
    else:
        print("Error")

    #7

    sum_1 = float(input("введите сумму покупки"))

    if (sum_1 >= 200) and (sum_1 < 300):
        print(0.03 * sum_1)

    elif (sum_1 >= 300) and (sum_1 < 500):
        print(0.05 * sum_1)

    elif sum_1 >= 500:
        print(0.07 * sum_1)
    else:
        print("на эту сумму нет скидки")

    #8

    S = int(input("введите площадь квадрата:"))
    l = int(input("введите длину окружности:"))
    if (l/3.14) == (S ** 0.5):
        print("yes")

    else:
        print("no")

    #9

    print("выберите правильный вариант ответа:")
    n_1 = int(input("S квадрата равна: 1)a^1 2)a^2 3)a^4. Ответ:"))
    n_2 = int(input("длина окружности равна: 1)2пr 2)2пr^2 3)пr^2 Ответ:"))
    n_3 = int(input("S окружности равна:1)2пr 2)2пr^2 3)пr^2 Ответ:"))
    ba = 0
    if n_1 == 2:
        ba = ba+2
    if n_2 == 1:
        ba = ba+2
    if n_3 == 3:
        ba = ba+2
    print(f"Ваши баллы:{ba}")

    #10

    day = int(input("введите день:"))
    month = int(input("введите месяц:"))
    year = int(input("введите год:"))
    dim = 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        dim = 30
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            dim = 29
        else:
            dim = 28

    if day < dim:
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
    print(f"следующая дата:{day},{month},{year}")
homework_3()

