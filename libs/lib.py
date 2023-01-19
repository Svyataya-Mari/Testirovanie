# Функция алгоритма сортировки пузырьком
# Принимает a - последовательность чисел
# Пример:
# [10, 2, 6, 4, 3] -> [2, 3, 6, 4, 10]
def sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Функция калькулятора принимает 3 аргумента: число 1, число 2 и знак
# действия: +, -, *, / выполняет действие и возвращает результат
# Пример:
# 2+2 -> 4
# 20-5 -> 15
# 5*5 -> 25
# 6/2 -> 3
def calc(a, b, sign):
    if (sign == "+"):
        return a+b
    elif (sign == "-"):
        return a-b
    elif (sign == "*"):
        return a*b
    elif (sign == "/"):
        return a/b

# Функция определения n чисел Фибоначчи
# Принимает n
# Возвращает список чисел Фибоначчи от 1 до n
# Пример: 7 -> 1, 1, 2, 3, 5, 8, 13
def fib(n):
    fib1 = fib2 = 1
    fibl = []
    while n > 0:
        fibl.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fibl