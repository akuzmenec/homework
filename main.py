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



