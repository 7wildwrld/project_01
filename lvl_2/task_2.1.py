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