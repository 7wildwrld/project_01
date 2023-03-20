def remove_exclamation_marks(s):
  s = s.replace('!','')
  print(s)

string = input('Введите текст: ')
remove_exclamation_marks(string)


def remove_last_em(s):
  if s[-1] == '!':
    print(s[:-1])
  else:
    print(s)

string = input('Введите текст: ')
remove_last_em(string)

def remove_word_with_one_em(s):
  str1 = ''
  for item in s:
    em = 0
    for i in range(len(item)):
      if item[i] == '!':
        em += 1
    if em != 1:
      str1 += item
  print(str1)

string = input('Введите текст: ').split(' ')
remove_word_with_one_em(string)

# Да, вариант рабочий. Можно еще воспользоваться методом removesuffix('!') для второго пункта
