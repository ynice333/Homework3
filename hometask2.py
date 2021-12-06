# Cоздайте функцию, которая принимает три параметра.
# Первый и второй параметры должны быть числовымию
# Третий параметр должен быть равен тексту "add", "subtract", "multiply", "divide"
# Функция должна вернуть ответ, выполнив заданное арифметическое действие.
# Для решения примера следует использовать функцию eval.

def calculator(a, b, action):
    if action == 'add': return eval(f'{a} + {b}')
    if action == 'multiply': return eval(f'{a} * {b}')

print(calculator('4', '3', 'add'))
print(calculator('2', '6', 'multiply'))