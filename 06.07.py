a = int(input())
b = int(input())
ls1 = []
def create_list(ls1):
    for i in range(b):
        ls = []
        for j in range(a):
            ls += [int(input())]
        ls1 += [ls]
    return ls1


print(create_list(ls1))

def min_max_li(i1, j1, mx, mx_ind, mn, mn_ind):
    if ls1[i1][j1] > mx:
        mx = ls1[i1][j1]
        mx_ind = j1
    if ls1[i1][j1] < mn:
        mn = ls1[i1][j1]
        mn_ind = j1
    return i1, j1, mx, mx_ind, mn, mn_ind

def min_max_col(i1, j1, mx, mx_ind, mn, mn_ind):
    if ls1[i1][j1] > mx:
        mx = ls1[i1][j1]
        mx_ind = i1

    if ls1[i1][j1] < mn:
        mn = ls1[i1][j1]
        mn_ind = i1
    return i1, j1, mx, mx_ind, mn, mn_ind

def min_max_all(max_allf, min_allf, line_maxf, line_minf):
    if max_allf < max:
        max_allf = max
        line_maxf = ind_max
    if min_allf > min:
        min_allf = min
        line_minf = ind_min
    return max_allf, min_allf, line_maxf, line_minf

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
        i, j, max, ind_max, min, ind_min = min_max_li(i, j, max, ind_max, min, ind_min)

        max_all, min_all, line_max, line_min = min_max_all(max_all, min_all, line_max, line_min)


    print(f"|\t{sum}(sum)\t |{sum/a}(a.m)\t |{max}(max)\t |ind = {ind_max} |{min}(min) |ind = {ind_min}" )
print("----------")

col_max, col_min = 0, 0
for i in range(len(ls1[0])):
    sum1 = 0
    ind_max1, ind_min1 = 0, 0
    max1 = ls1[0][i]
    min1 = ls1[0][i]
    for j in range(len(ls1)):
        print(ls1[j][i], end="\t")
        sum1 += ls1[j][i]
        j, i, max1, ind_max1, min1, ind_min1 = min_max_col(j, i, max1, ind_max1, min1, ind_min1)
        max_all, min_all, col_max, col_min = min_max_all(max_all, min_all, col_max, col_min)
    print(f"|\t{sum1}(sum)\t |{sum1 / a}(a.m)\t |{max1}(max)\t |ind = {ind_max1} |{min1}(min) |ind = {ind_min1}")
print("----------")

print(f"сумма всех значений:{sum_all}, среднее:{sum_all/len(ls1[0]*len(ls1))}, максимальное:{max_all}|ind = line:{col_max+1} col:{line_max+1},  минимальное:{min_all}|ind = line:{line_min+1} col:{col_min+1}")