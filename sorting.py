from pickletools import read_stringnl_noescape

ls = [9, 8, 7, 6, 5]

def swap(ls, ind1, ind2):
    ls[ind1], ls[ind2] = ls[ind2], ls[ind1]


def bubble_sort(ls):
    for j in range(len(ls)-1):
        flag = False
        for i in range(len(ls) - 1 - j):
            if ls[i] > ls[i+1]:
                swap(ls, i, i+1)
                flag = True
        if not flag:
            break
    return ls
#print(bubble_sort(ls))


def ins_sert(ls):

    for i in range(1, len(ls)):
        for j in range(i, 0, -1):
            if ls[j] < ls[j-1]:
                swap(ls, j, j-1)
            else:
                break
    return ls
# print(ins_sert(ls))


def shaker_sort(ls):

    for i in range(len(ls)-1):
        flag = False
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j+1]:
                swap(ls, j, j+1)
                flag = True
        if flag:
            for g in range(len(ls) - 2 - i , i, -1):
                if ls[g] < ls[g-1]:
                    swap(ls, g, g-1)
        else:
            break
    return  ls

#print(shaker_sort(ls))

def select_sort(ls):

    for i in range(len(ls)-1):
        ind = i

        for j in range(i + 1, len(ls)):
            if ls[j] < ls[ind]:
                ind = j
        if ind != i:
            ls[i], ls[ind] = ls[ind], ls[i]
    return ls

print(select_sort(ls))



















