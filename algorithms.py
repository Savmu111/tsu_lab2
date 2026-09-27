def sum_odd_nums(n: int) -> int:
    if n < 1:
        return 0

    total = 0
    for number in range(1, n + 1):
        if number % 2 != 0:
            total += number
    return total


def euclidean(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def euclidean_recursive(a: int, b: int) -> int:
    a, b = abs(a), abs(b)

    if b == 0:
        return a
    
    return euclidean_recursive(b, a % b)


def num_of_vowels(text: str) -> int:
    vowels = 'аеёиоуыэюяaeiouy'
    text = text.lower()

    count = 0
    for char in text:
        if char in vowels:
            count += 1

    return count
