from random import randint
k = 0
com = randint(1, 99)
print(com)
w = 0
l = 0
while k != 5:
    k += 1
    num_1 = int(input("угадайте число:"))
    if num_1 == com:
        print("вы выйграли!")
        w += 1
    elif com > num_1:
        print("загаданное число больше!")
        l += 1
    else:
        print("загаданное число меньше!")
        l += 1

    if k == 5:
        print("игра закончена")
        n = int(input("если хотите продолжить игру введите 0 :"))
        if n == 0:
            k = 0
        else:
            break
    else:
        print(f"осталсь попыток: {5 - k}")

print(f"вы выйграли раундов: {w} , компьютер: {l} ")

