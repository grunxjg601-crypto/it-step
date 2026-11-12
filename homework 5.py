
import colorama

colorama.init()

print("ДОСЛІДЖЕННЯ БІБЛІОТЕКИ COLORAMA")

print(" Атрибути бібліотеки:")
for item in dir(colorama):
    if not item.startswith("_"):
        print(item)

print(" Найважливіші атрибути:")
print("Fore - змінює колір тексту")
print("Back - змінює колір фону")
print("Style - змінює стиль тексту")
print("Cursor - керує курсором")

print(" Основні методи:")
print("init() - налаштовує бібліотеку")
print("deinit() - вимикає її роботу")
print("reinit() - повторно вмикає її")

print(" Приклад використання:")
print(colorama.Fore.RED + "Червоний текст")
print(colorama.Fore.GREEN + "Зелений текст")
print(colorama.Fore.BLUE + "Синій текст")
print(colorama.Style.RESET_ALL + "Звичайний текст")
