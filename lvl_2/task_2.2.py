def quarter_of(month):
  months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
  q = (month - 1) // 3 + 1
  text = ['первого', 'второго', 'третьего', 'четвертого']
  print('Месяц', month, '(' + months[month - 1] + ') является частью', text[q - 1], 'квартала')

num = int(input('Введите номер месяца: '))
quarter_of(num)