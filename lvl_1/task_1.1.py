my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
x = my_favorite_songs.find(',')
y = my_favorite_songs.rfind(',')
z = my_favorite_songs.find(',', x + 1)
s = my_favorite_songs.rfind(',', z, y)
print(my_favorite_songs[:x], end=' ')
print(my_favorite_songs[y + 2:], end=' ')
print(my_favorite_songs[x + 2:z], end=' ')
print(my_favorite_songs[s + 2:y], end=' ')

# Отлично!
# Альтернативный вариант. мы можем воспользоваться методом разделения строк по символам. split.
# Полученный в результате список проиндексируем по песням

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
