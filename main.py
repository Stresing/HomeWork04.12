# напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def Task1():# дополнительно проработать, избавиться от запятой
    numb = input("Введите число: ")
    numb.isdigit()
    sum_numb = 0
    for i in numb:
        sum_numb = sum_numb + int(i)
    print(sum_numb)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def Task2():
    num = input("Введите число: ")
    sum_product = 1
    for i in range(1, int(num) + 1):
        sum_product = sum_product * i
        print(sum_product)


# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
def Task3():
    num = input()  # 5
    sim = 0
    sum = 0
    for i in range(1, int(num) + 1):
        sim = round(((1 +1 / i) ** i), 2)
        sum = sum + sim
        print(sim)

    print(f"сумма всех чисел равна:{sum}")
# (1+(1\n)^n

task = int(input("Введите задание которое хотите просмотреть: "))
if task == 1:
    Task1()
elif task == 2:
    Task2()
elif task == 3:
    Task3()
