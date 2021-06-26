def problem1():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--hours', type=int, help='Working hours amount')
    parser.add_argument('--hourly_rate', type=int, help='Employee hourly rate')
    parser.add_argument('--bonus', type=int, help='Bonus for good work')

    args = parser.parse_args()
    print('Result:', args.hours * args.hourly_rate + args.bonus)


def problem2():
    try:
        numbers = list(map(int, input('Enter list of numbers: ').split()))
    except ValueError:
        print('Error! Cannot parse input numbers')
        return

    res = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
    print('Result:', res)


def problem3():
    try:
        a, b = map(int, input('Enter two numbers: ').split())
    except ValueError:
        print('Error! Cannot parse input numbers')
        return

    res = [i for i in range(a, b + 1) if i % 20 == 0 or i % 21 == 0]
    print('Result:', res)


def problem4():
    from collections import Counter

    try:
        nums = map(int, input('Enter list of numbers: ').split())
    except ValueError:
        print('Error! Cannot parse input numbers')
        return

    counter = Counter(nums)
    res = [number for number in counter if counter[number] == 1]
    print('Result:', res)


def problem5():
    import functools

    from_num, to_num = 100, 1000
    res = functools.reduce(lambda a, b: a * b, range(from_num, to_num + 1, 2))
    print('Result:', res)


def problem6_1():
    import itertools

    def gen_function(a, b=None):
        counter = itertools.count(a)
        while True:
            num = next(counter)
            yield num
            if b is not None and num >= b:
                break

    try:
        from_num, to_num = map(int, input('Enter two numbers: ').split())
    except ValueError:
        print('Error! Cannot parse input numbers')
        return

    print('Result:')
    for number in gen_function(from_num, to_num):
        print(number)


def problem6_2():
    import itertools

    def gen_function(elements, max_repeats=None):
        counter = itertools.cycle(elements)
        repeats = 0
        while True:
            num = next(counter)
            repeats += 1
            yield num
            if max_repeats is not None and repeats >= max_repeats:
                break

    inp = input('Enter list of elements: ').split()

    print('Result:')
    for number in gen_function(inp, 100):
        print(number)


def problem7():
    def fact(num=None):
        res = 1
        multiplier = 1
        while True:
            res *= multiplier
            yield res
            if num is not None and multiplier >= num:
                break
            multiplier += 1

    try:
        n = int(input('Enter a number: '))
    except ValueError:
        print('Error! Cannot parse input number')
        return

    print('Result:')
    for el in fact(n):
        print(el)


if __name__ == '__main__':
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6_1()
    problem6_2()
    problem7()
