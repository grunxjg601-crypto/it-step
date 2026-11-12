
try:
    number = input("Введіть число: ")
    number = int(number)
    print("Ваше число:", number)

except ValueError:
    print("Помилка! Ви ввели не число.")
