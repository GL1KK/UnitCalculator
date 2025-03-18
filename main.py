print("Введите первое число")
try:
    value1 = int(input())
except:
    print("Не корректный ввод")
print("Введите второе число")
try:
    value2 = int(input())
except:
    print("Не корректный ввод")
print("Введите знак действия(+ / * -  **)")
do = input()
if do == "+":
    result = value1 + value2
    print(result)
if do == "/":
    result = value1 / value2
    print(result)
if do == "*":
    result = value1 * value2
    print(result)
if do == "-":
    result = value1 - value2
    print(result)
if do == "**":
    result = value1 ** value2
    print(result)
else:
    print("Введите корректный запрос")
