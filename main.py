from algorithms import (sum_odd_nums, euclidean,
                        euclidean_recursive, num_of_vowels)


def main() -> None:
    print('Лабораторная работа №2. 2 вариант\n')

    n = int(input('Введите N для 1 задания: '))
    res = sum_odd_nums(n)
    print(f'Сумма нечетных чисел до {n}: {res}')

    num1, num2 = map(int, input('Введите num1 и num2 для НОД по Евклиду: ')
                     .split(' '))
    res = euclidean(num1, num2)
    print(f'НОД({num1}, {num2}) по Евклиду: {res}')
    res = euclidean_recursive(num1, num2)
    print(f'НОД({num1}, {num2}) по Евклиду рекурсивным методом: {res}')

    text = input('Введите текст для подсчета гласных: ')
    res = num_of_vowels(text)
    print(f'Кол-во гласных в "{text}": {res}')


if __name__ == '__main__':
    main()
