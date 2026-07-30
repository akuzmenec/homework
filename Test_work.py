from random import randint
# #1
# a = int(input())
# max = a
# for i in range(4):
#     a = int(input())
#     if a > max:
#         max = a
# print(max)

# #2
# a = int(input())
# b = int(input())
# if a > b:
#     a,b = b,a
# for i in range(b, a+1, -1):
#     print(i)

# #3
#
# counter = 5
# a = int(input())
# for j in range(a):
#     for i in range(a):
#         print(counter, end="\t")
#         counter += 1
#     print()

# #4
# sym = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z "
# a = input()
# if a in sym:
#     print(True)
# else:
#     print(False)

# #5
#
# ls = []
# for i in range(8):
#     ls.append(i*3)
# print(ls)


# #6,7
# row = int(input())
# col = int(input())
# if row>col:
#     row,col = col,row
# ls = [[], []]
# for i in range(5):
#     ls[0].append(randint(row, col))
#     ls[1].append(randint(row, col))
# print(ls)
# avg = (sum(ls[0]) + sum(ls[1])) / 10
# print(avg)
#
# min = [0][0]
# max = [0][0]
#
# for i in range(len(ls)):
#     for j in range(len(ls[i])):
#         if ls[i][j] > max:
#             max = ls[i][j]
#         if ls[i][j] < min:
#             min = ls[i][j]

# #8
#
# ls = [1, 2, 3, 4, 5]
# a = int(input())
# def in_ls(a, ls):
#     flag = "no"
#     for i in ls:
#         if a == i:
#             flag = "yes"
#             break
#     return flag
#
#
# print(in_ls(a, ls))

# #9
# ls = [1, 2, 3, 4, 5]
# def type_num(ls):
#     num = []
#     for i in ls:
#         if i%2 == 0:
#             num.append(i)
#     return num
#
# print(type_num(ls))

# #10
# ls = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# ind = int(input())
# def ret_mat(ls, ind):
#     a = []
#     for i in range(len(ls)):
#         a.append(ls[i][ind-1])
#     return a
# print(ret_mat(ls, ind))

# #11
#
# st = "hello 10 120 1 world"
# def num_in_str(st):
#     a = []
#     st = st.split()
#     for i in st:
#         if str(i).isdigit():
#             a.append(i)
#     return a
# print(num_in_str(st))



# #12
# class_st = {}
# marks = []
# while True:
#     cm = input("add, remove, add_mark, list_class, list_st, list_all, exit: ")
#     if cm == "exit":
#         break
#
#     elif cm == "add":
#         cl = int(input("введите номер класса:"))
#         if cl in class_st.keys():
#             class_st[cl].append(input("введите имя:"))
#         else:
#             class_st.update({int(input("ведите класс:")): [input("введите имя:")]})
#         marks.append([])
#
#     elif cm == "add_mark":
#         ind = int(input("введите номер студента:"))
#         if ind<=0 and ind > len(marks):
#             print("нет студента!")
#         else:
#             marks[ind-1].append(int(input("введите оценку:")))
#
#     elif cm == "remove":
#         cl = int(input("введите класс:"))
#         name = input("введте имя: ")
#         ind = int(input("введите номер студента: "))
#         class_st[cl].remove(name)
#         del marks[ind-1]
#
#     elif cm == "list_class":
#         cl = int(input("введите класс:"))
#         print(class_st[cl])
#
#     elif cm == "list_st":
#         cl = 0
#         ind = int(input("введите номре ст: "))
#         name = input("введите имя:")
#         for k, v in class_st.items():
#             if name in v:
#                 cl = k
#         print(f"класс: {cl}, имя: {name}, оценки: {marks[ind-1]}")
#
#     else:
#         print("команда не найдена!")















