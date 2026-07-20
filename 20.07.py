students = {}
while True:

    cm = input("add, remove, list, exit: ")

    if cm == "exit":
        break

    elif cm == "add":
        name = (input("введите имя студента: "))
        hobby = {input("ведите увлечения студента: ")}
        students.update({name: hobby})

    elif cm == "remove":
        name = input("введите имя ученика:")
        if name in students:
            students.pop(name)
        else:
            print("студент не найден")

    elif cm == "list":
        for i in students.keys():
            print(f"{i} - {students[i]}")

    else:
        print("команда не найдена!")

