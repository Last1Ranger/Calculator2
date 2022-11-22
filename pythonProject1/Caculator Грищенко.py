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
    number1 = int(input(("Введите число, которое хотите конвертировать:")))
    operation = int(input("Введите номер операции"))
    if operation == 1:  # Операция сравнивается с её номером и выполняется соотвецтвенное действие, вслед за чем происходит вывод итога данной операции
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
    print("6. ")
    print("5. Возводить в степень")
    operation = input("Введите номер операции: ")
    if operation == 1:  # Операция сравнивается с её номером и выполняется соотвецтвенное действие, вслед за чем происходит вывод итога данной операции
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
    number1 = int(input("Введите сумму вклада:"))
    number2 = int(input("Введите срок вклада:"))
    number3 = int(input("Введите процент вклада:"))
    number12 = number1
    for x in range(number2):
        number1 = number1 + number1 * 0.01 * number3 / number2
    income = number1 - number12
    print(income)


elif a == 4:
    numder1 = int(input(("Введите число которое хотите перевести в деятичную систему счисления:")))
    numder2 = int(input("Введите систему счисления вашего числа:"))
    print(int(numder1, numder2))
