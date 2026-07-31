def number_sequence(start, end, even = True):
    return [
        i for i in range(start, end + 1)
        if (even and i%2 == 0) or (not even and i%2 != 0)
    ]
try:
    start = int(input("введите начало диапазона: "))
    end = int(input("введите конец диапазона: "))
    if start > end:
        start, end = end, start
    even1 = input("ведите тип последовательности (четные\нечетные):").strip().lower()
    even = even1 == "четные"
    print(f"последовательность: {number_sequence(start, end, even)}")
except ValueError:
    print("Ошибка: вводите только целые числа!")


