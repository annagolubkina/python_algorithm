"""По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки."""

x1 = float(input("Введите координату X первой точки: "))
y1 = float(input("Введите координату Y первой точки: "))
x2 = float(input("Введите координату X второй точки: "))
y2 = float(input("Введите координату Y второй точки: "))

if x1 == x2:
    print(f"Прямая параллельна оси ординат и имеет вид x = {x1}")
else:
    if y1 == y2:
        print(f"Прямая параллельна оси абсцисс и имеет вид y = {y1}")
    else:
        k = (y1 - y2) / (x1 - x2)
        print(f"Уравнение прямой проходящей через точки: "
              f"({x1}, {y1}), ({x2}, {y2}) y = {k} * x + {y2 - k * x2}")
