"""
3 зміних:
1- посада
2- річна зарплата
3- % підвищення
Зваданя:
1- місячна зарплата до підвищення
2- річна після підвищення
"""

position = input('введіть посаду: ')
print("Ваша посада", position)
salary = float(input('Введіть вашу зарплату:'))
print(" Ваша зарплата", salary)
percentage = float(input("Ваш процент: "))
print ("процент підвищення зарплати ", percentage)

monthly_payment = salary/12
print(" Ваша місячна зарплата", monthly_payment )


after_promotion = ((100 + percentage) * salary)/ 100
print(" Ваша річна зарплата після підв", after_promotion )
