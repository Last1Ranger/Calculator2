print("1. Включить конвертер")
print("2. Включить калькулятор")
print("3. Расчитать доходность вклада")
print("4. Перевести число из различных систем счисления в десятичную")
a = int(input())

if a == 1:
    print("Эта программа умеет:")
    print("1. Переводить из грамм в килограммы")
    print("2. Переводить из килограмм в граммы")
    print("3. Переводить из сантиметров в метры")
    print("4. Переводить из метров в сантиметры")
    number1 = int(input("Введите число, которое хотите конвертировать:"))
    operation = int(input("Введите номер операции"))
    if operation == 1:  # Операция сравнивается с её номером и выполняется соотвецтвенное действие, вслед за чем
        # происходит вывод итога данной операции
        print(number1 / 100)
    elif operation == 2:
        print(number1 * 100)
    elif operation == 3:
        print(number1 / 100)
    elif operation == 4:
        print(number1 * 100)

elif a == 2:
    number1 = int(input("Введите 1-е число:"))  # Ввод первого числа
    number2 = int(input("Введите 2-е число:"))  # Ввод второго числа
    print("Эта программа умеет:")  # пердставляется выбор операций
    print("1. Уиножать")
    print("2. Делить")
    print("3. Вычислять остаток от деления")
    print("4. Выполнять целочисленное деление")
    print("5. Возводить в степень")
    operation = input("Введите номер операции: ")
    if operation == 1:  # Операция сравнивается с её номером и выполняется соотвецтвенное действие, вслед за чем
        # происходит вывод итога данной операции
        print(number1 * number2)
    elif operation == 2:
        print(number1 / number2)
    elif operation == 3:
        print(number1 % number2)
    elif operation == 4:
        print(number1 // number2)
    elif operation == 5:
        print(number1 ** number2)


elif a == 3:
    amount = int(input("Введите сумму вклада(руб):"))
    age = int(input("Введите срок вклада(мес):"))
    percent = int(input("Введите процент вклада(%):"))
    first_amount = amount
    percent = percent / 12
    for x in range(age):
        amount = amount + (amount / 100 * percent)  # Расчёт доходности вклада по формуле
    income = amount - first_amount
    print("Доход вашего вклада составил:", int(income), "(руб)")


elif a == 4:
    number1 = int(input("Введите число которое хотите перевести в деятичную систему счисления:"))
    number2 = int(input("Введите систему счисления вашего числа:"))
    # noinspection PyTypeChecker
    print(int(number1, number2))  # С помощью функции int переводим число из любой системы
    # счисления в десятичную
