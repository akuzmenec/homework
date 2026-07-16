students = []
marks = []
while True:
    cm = int(input("1 - добавить ст, 2 - удалить ст, 3 - добавить оценки ,4 - исправить оценки ,5 - вывести инф, 6 - выход"))

    if cm == 1:
        name = input("введите имя:")
        students.append(name)
        marks.append([])

    elif cm == 2:
        ind = int(input("введите номер ст:"))
        if 1<=ind<=len(students):
            students.pop(ind - 1)
            marks.pop(ind - 1)
        else:
            print("нет студента")

    elif cm == 3:
        ind = int(input("введите номер ст:"))
        if 1 <= ind <= len(students):
            mark = int(input("введите оценку:"))
            marks[ind - 1].append(mark)
        else:
            print("нет студента")

    elif cm == 4:
        ind = int(input("введите номер ст:"))
        if 1 <= ind <= len(students):
            ind_mark = int(input("введите номер оценки:"))
            if len(marks[ind - 1]) < ind_mark:
                print("нет оценки")
            else:
                mark = int(input("введите оценку:"))
                marks[ind - 1][ind_mark] = mark

        else:
            print("нет студента")
    elif cm == 5:
        for i in range(len(students)):
            print(f"студент:{students[i]}, оценки:{marks[i]}")
    else:
        break






