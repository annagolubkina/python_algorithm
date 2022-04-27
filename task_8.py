m = 5
n = 4
matrix_a = []

for i in range(n):
    matrix_b = []
    sum = 0
    print("строка %d:" % i)
    for j in range(m - 1):
        n = int(input())
        sum += n
        matrix_b.append(n)
    matrix_b.append(sum)
    matrix_a.append(matrix_b)

for i in matrix_a:
    print(i)
    