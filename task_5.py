"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
import random

my_list = [random.randint(-5, 5) for _ in range(10)]
print(my_list)
neg_list = []

for i, item in enumerate(my_list):
    if item < 0:
        neg_list.append(item)
max_el = neg_list[0]

for idx in range(1, len(neg_list)):
    if neg_list[idx] > max_el:
            max_el = neg_list[idx]
print(f'Максимальный отрицательный элемент {max_el}')