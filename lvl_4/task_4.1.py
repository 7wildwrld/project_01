# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12KFBH1moRZmkR2U-97zchLCnNEz4mAlC
"""

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_info(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT st.Student_Id, st.Student_Name, sc.School_Id, sc.School_Name FROM Students st 
    join School sc on st.School_Id=sc.School_Id
    WHERE st.Student_Id = ?"""
    cursor.execute(select_query,(student_id,))
    record = cursor.fetchone()
    close_connection(connection)
    print('ID студента: ' + str(record[0]), 'Имя студента: ' + record[1], 'ID школы: ' + str(record[2]), 'Название школы: ' + record[3], sep='\n')
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных", error)

id = int(input('Введите ID студента: '))
get_info(id)