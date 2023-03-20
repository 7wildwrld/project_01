def minimum(arr):
    min_num = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
    print('min =', min_num)


def maximum(arr):
    max_num = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    print('max =', max_num)


listNum = []
for i in input('Введите список чисел: ').split(','):
    listNum.append(int(i))
minimum(listNum)
maximum(listNum)

# Хорошо! У вас вариант с сортировкой выбором
# Решение задачи с помощью быстрой сортировки 

def quicksort(arr):
    if len(arr) < 2:
        # базовый случай, массив с 0 или 1 элементом уже отсортирован
        return arr
    else:
        # рекурсивный случай. выберем опорный элемент pivot
        pivot = arr[0]
        # подмассив всех элементов, меньших, чем опорный элемент pivot
        less = [i for i in arr[1:] if i <= pivot]
        # подмассив всех элементов, превышающих опорный элемент pivot
        greater = [i for i in arr[1:] if i > pivot]
        # обединяем в порядке "сортировка для меньшего подмассива – опорный элемент – сортировка для большего подмассив"
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]

print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
