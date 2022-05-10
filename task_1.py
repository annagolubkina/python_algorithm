"""В диапазоне натуральных чисел от 2 до 99 определить,сколько из них кратны каждому из чисел в диапазонеот 2 до 9."""
arr = list(range(2, 100))

div_two = div_three = div_four = div_five = div_six = div_seven = div_eight = div_nine = 0

for item in arr:
    if not item % 2:
        div_two += 1
    if not item % 3:
        div_three += 1
    if not item % 4:
        div_four += 1
    if not item % 5:
        div_five += 1
    if not item % 6:
        div_six += 1
    if not item % 7:
        div_seven += 1
    if not item % 8:
        div_eight += 1
    if not item % 9:
        div_nine += 1
print(arr)
print(div_two, div_three, div_four, div_five, div_six, div_seven, div_eight, div_nine )
