str1 = "hello world 12 123 1 "
str2 = "hello world hello"

def counter_words(str1):
    k = 0
    str1 = str1.split(" ")
    for i in str1:
        if i.isalpha():
            k += 1
    return k

print(counter_words(str1))


def counter_num(str1):
    k = 0
    for i in str1.split(" "):
        if i.isdigit() and int(i)//10 > 0:
            k += 1
    return k

print(counter_num(str))


def repeated_words(str2):
    st = ""
    for i in str2.split(" "):
        if (str2.split(" ")).count(i) > 1 and i not in st:
            st += i
    return st
print(repeated_words(str2))


