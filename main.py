def max_sum_digits():
    max_sum = -1
    max_nums = []

    print("Введите целые числа через Enter, для завершения ввода, введите 0")

    while True:
        try:
            num = int(input())
            if num == 0:
                break
            digits_sum = sum([int(digit) for digit in str(abs(num))])
            if digits_sum > max_sum:
                max_sum = digits_sum
                max_nums = [num]
            elif digits_sum == max_sum:
                max_nums.append(num)

        except ValueError:
            print("Неподходящий тип данных, используйте целые числа")

    if len(max_nums) == 0:
        print("Нет введенных значений")

    if len(max_nums) > 1:
        print("Наибольшая сумма цифр одинакова в числах", ', '.join(map(str, max_nums)))
    elif len(max_nums) == 1:
        print("Наибольшая сумма цифр в числе", ', '.join(map(str, max_nums)))


if __name__ == "__main__":
    max_sum_digits()
    input()
    print("Для продолжения ввода перезапустите программу")
    input()