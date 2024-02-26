print("Добро пожалавать в калькулятор")

num1 = float(input("Введите первое число : "))
num2 = float(input("Введите второе число : "))

operation = input("Введите опнрацию (+,-,/,*):")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == '/':
    result = num2 / num2
elif operation == "*":
    result  = num1 * num2

else:
    print("НЕправильный ввод")
    quit()

print("Результат:", result)



