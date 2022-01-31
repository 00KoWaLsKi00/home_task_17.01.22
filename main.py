#
# """
# DRY - don't repeat yourself!!!  --> не повторюй свій код!
# YAGNI - you ain't gonna need it --> тобі це не знадобиться
# SOLID - >
# """
#
# """
# Якщо в тебе код повторюється хоча б 2 рази, то ти пишеш функцію!
# """
#
#
# #s = None
#
# """14 - 45 функції, які нічого не повертають мають тип даних None"""
# # s1 = input("Input string:")
# #
# # def print_something():       # оголошуємо функцію без параметрів!
# #     """
# #     This function prints 50 times string x 5
# #     """
# #     for i in range(50):
# #         print(s1 * 5)
# #     print("END")
# #
# # print_something()
# # print_something()
#
#
#
# # def sum_two_nums(num1, num2):           # реалізувати * / // % ** двух числе
# #     print(f"Number1 + Number2 = {num1+num2}")
# #
# # sum_two_nums(11,25)
# #
#
#
# # num1 = 15       # знаходиться в глобальному просторі імен -> я можу всюди до неї достукатись
# #
#
# # def foo():
# #     num1 = 11
# #     print(num1)
# #     s = "Hello"
# #     # ті змінні які ми оголошуємо у функції - локальні
# #
# #
# # print(foo())    # not exactly correct!
#
#
#
# # def calculator(num1, num2):       #setattr  --> OOP
# #     res = num1 + num2
# #     return res  # повертає значення
# #
# # """Если функция что-то возвращает, то это значение нужно где-то хранить"""
# # res = calculator(11,22)
# # print(res)
#
#
# # def input_name():
# #     name = input("Hello, enter your name:")
# #     return name
# #
# # name = input_name()
# # print(name)
#
# """
# Создать функцию, которая будет выступать в качестве калькулятора
# На вход она принимает 2 числа + знак ,  проверяет какой знак и выполняет ар операцию
# """
# """
#
# Создать функцию, которая будет выступать в качестве калькулятора
# На вход она принимает 2 числа + знак ,  проверяет какой знак и выполняет ар операцию
# """
#
# def calculator(num1, num2, znak):
#     if znak == '+':
#         return num1+num2
#     elif znak == '-':
#         return num1-num2
#     elif znak == '/':
#         return num1/num2
#     elif znak == '*':
#         return num1*num2
#     elif znak == '**' or znak == '^':
#         return num1**num2
#     elif znak == '//':
#         return num1//num2
#     elif znak == '%':
#         return num1%num2
# n = calculator(int(input()), int(input()), input())
# print(n)

"""
Написать функцию, которая принимает 4 параметра:
1 - строка
2 - начало(среза)
3 - конец(среза)
4 - шаг
Нужно создать отдельную функцию, которая проверяет валидность данных и вызвать её внутри функции
"""

def get_slice(str1:str, start:int, end:int, step:int):
    """

    :param str1:
    :param start:
    :param end:
    :param step:
    :return:
    """
    flag = Tru
    return str1[start:end:step]

def validation(start:int, end:int, step:int):
    if (start > end and step > 0) or ( step < 0 and end > start ) :
        return True
    return False

