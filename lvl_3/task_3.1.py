import random

class Matrix():
  def __init__(self, row_count, column_count):
    self.r_count = row_count
    self.c_count = column_count
    self.placeholder = ['yes']

  def print_matrix(self):
    nested_list = [[random.choice(self.placeholder) for i in range(self.c_count)] for i in range(self.r_count)]
    print(str(nested_list).replace(', [', ',\n ['))

  def change_count(self, new_row_count, new_column_count):
    self.r_count = new_row_count
    self.c_count = new_column_count

  def change_placeholder(self, list1):
    self.placeholder = list1

  def print_row_and_column_count(self):
    print('Число строк ' + str(self.r_count) + '\nЧисло столбцов ' + str(self.c_count))


matrix_1 = Matrix(9, 3)
matrix_1.print_matrix()
print('\n')
matrix_1.change_count(8, 9)
matrix_1.print_matrix()
print('\n')
matrix_1.change_placeholder([1, 2, 'f'])
matrix_1.print_matrix()
print('\n')
matrix_1.print_row_and_column_count()