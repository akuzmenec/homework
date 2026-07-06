a = int(input())
b = int(input())
ls1 = []
for i in range(b):
    ls = []
    for j in range(a):
        ls += [int(input())]
    ls1 += [ls]
print(ls1)

sum_all, max_all = 0, 0
min_all = ls1[0][0]
line_max, line_min = 0, 0
for i in range(len(ls1)):
    sum = 0
    ind_max, ind_min = 0, 0
    max = ls1[i][0]
    min = ls1[i][0]
    for j in range(len(ls1[i])):
        print(ls1[i][j], end="\t")
        sum += ls1[i][j]
        sum_all += ls1[i][j]
        if ls1[i][j] > max:
            max = ls1[i][j]
            ind_max = j
        if ls1[i][j] < min:
            min = ls1[i][j]
            ind_min = j
    if max_all < max:
        max_all = max
        line_max = ind_max
    if min_all > min:
        min_all = min
        line_min = ind_min


    print(f"|\t{sum}(sum)\t |{sum/a}(a.m)\t |{max}(max)\t |ind = {ind_max} |{min}(min) |ind = {ind_min}" )
print("----------")

col_max, col_min = 0, 0
for i in range(len(ls1[0])):
    sum1 = 0
    max1 = ls1[i][0]
    min1 = ls1[i][0]
    ind_max1, ind_min1 = 0, 0
    for j in range(len(ls1)):
        print(ls1[j][i], end="\t")
        sum1 += ls1[j][i]
        if ls1[j][i] > max1:
            max1 = ls1[j][i]
            ind_max1 = j
        if ls1[j][i] < min1:
            min1 = ls1[j][i]
            ind_min1 = j
        if max1 == max_all:
            col_max = ind_max1
        if min1 == min_all:
            col_min = ind_min1
    print(f"|\t{sum1}(sum)\t |{sum1 / a}(a.m)\t |{max1}(max)\t |ind = {ind_max1} |{min1}(min) |ind = {ind_min1}")
print("----------")

print(f"сумма всех значений:{sum_all}, среднее:{sum_all/len(ls1[0]*len(ls1))}, максимальное:{max_all}|ind = line:{line_max+1} col:{col_max+1},  минимальное:{min_all}|ind = line:{line_min+1} col:{col_min+1}")