month = int(input('Введите номер месяца: '))
num1, num2, num3 = 28, 30, 31
days_30 = [4, 6, 9, 11]
days_31 = [1, 3, 5, 7, 8, 10, 12]
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if month == 2:
  print('Вы ввели', months[1] + '.', num1, 'дней')
elif month in days_30:
  print('Вы ввели', months[month - 1] + '.', num2, 'дней')
elif month in days_31:
  print('Вы ввели', months[month - 1] + '.', num3, 'дней')
else:
  print('Такого месяца нет!')  