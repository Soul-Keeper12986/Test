prev = 0
print("Введите числа через Enter, для завершения ввода, введите 0")

while next != 0:
    next = abs(sum(map(int, str(abs(int(input()))))))
    if next > prev:
        prev = next

print("Наибольшая сумма цифр в числе", prev)
input()
