"""4. Определить, какое число в массиве встречается чаще всего."""
import random

arr = [random.randint(-5,5) for _ in range(25)]
size = len(arr)
max_cnt = 1
item = arr[0]

for i in range(size - 1):
    cnt = 1
    for j in range(i + 1, size):
        if arr[i] == arr[j]:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            item = arr[i]

print(f'исходный массив:{arr}')
print(f'число {item} повторяестся {max_cnt} раз')
