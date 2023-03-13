import random
import datetime
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
sumMinutes = 0
sumSeconds = 0

for item in random.choices(my_favorite_songs, k = 3):
  d = "{:.2f}".format(item[1])
  minutes = int(d[0:1])
  seconds = int(d[2:4])
  sumMinutes += minutes
  sumSeconds += seconds


min_1 = sumSeconds // 60
sec_1 = sumSeconds % 60

print('Три песни звучат', str(sumMinutes + min_1)+ '.' + (str(sec_1) if len(str(sec_1)) == 2 else '0' + str(sec_1)), 'минут')

dt = datetime.time(0, sumMinutes + min_1, sec_1)
print('Три песни звучат', dt.strftime("%M:%S"), 'минут')


random_songs = random.choices(my_favorite_songs, k = 3)
print('Случайные песни:', [list[0] for list in random_songs])

import random
import datetime
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
sumMin = 0
sumSec = 0
for value in random.choices(list(my_favorite_songs_dict.values()), k = 3):
  d = "{:.2f}".format(value)
  min = int(d[0:1])
  sec = int(d[2:4])
  sumMin += min
  sumSec += sec
min_1 = sumSec // 60
sec_1 = sumSec % 60
print('Три песни звучат', str(sumMin + min_1) + '.' + (str(sec_1) if len(str(sec_1)) == 2 else '0' + str(sec_1)), 'минут')
dt = datetime.time(0, sumMin + min_1, sec_1)
print('Три песни звучат', dt.strftime("%M:%S"), 'минут')
random_songs = random.choices(list(my_favorite_songs_dict.keys()), k = 3)
print('Случайные песни:', random_songs)