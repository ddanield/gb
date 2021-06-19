from collections import defaultdict


def problem1():
    a = [1, 1.2, [4, 5], None, {'a': 1, 'b': 2}, {1, 2, 3}]
    for el in a:
        print(f'Type of {el} is {type(el)}')


def problem2():
    l = input().split()
    for i in range(1, len(l), 2):
        l[i], l[i - 1] = l[i - 1], l[i]

    print('Result: {}'.format(' '.join(l)))


WINTER = 'Winter'
SPRING = 'Spring'
SUMMER = 'Summer'
AUTUMN = 'Autumn'


def problem3_1():
    months = {
        12: WINTER, 1: WINTER, 2: WINTER,
        3: SPRING, 4: SPRING, 5: SPRING,
        6: SUMMER, 7: SUMMER, 8: SUMMER,
        9: AUTUMN, 10: AUTUMN, 11: AUTUMN,
    }
    n = int(input('Enter a number of month: '))
    print(f'Result: {months.get(n)}')


def problem3_2():
    months = [
        WINTER, WINTER,
        SPRING, SPRING, SPRING,
        SUMMER, SUMMER, SUMMER,
        AUTUMN, AUTUMN, AUTUMN,
        WINTER,
    ]
    n = int(input('Enter a number of month: '))
    if 1 <= n <= 12:
        print(f'Result: {months[n - 1]}')
    else:
        print(f'Month with number {n} does not exist!')


def problem4():
    words = input('Enter a words list: ').split()
    for idx, word in enumerate(words):
        print(f'{idx}: {word[:10]}')


def problem5():
    ratings = []
    while True:
        elem = input()
        if elem.lower() == 'stop':
            break
        elem = int(elem)
        insert = False
        if len(ratings):
            for i in range(len(ratings)):
                if elem > ratings[i]:
                    ratings.insert(i, elem)
                    insert = True
                    break
        if not insert:
            ratings.append(elem)

    print('Result: {}'.format(' '.join(map(str, ratings))))


def problem6():
    products = [
        (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
        (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
        (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
    ]
    stats = defaultdict(list)
    for product in products:
        for key, value in product[1].items():
            if value not in stats[key]:
                stats[key].append(value)

    print(f'Result: {stats}')


if __name__ == '__main__':
    problem1()
    problem2()
    problem3_1()
    problem3_2()
    problem4()
    problem5()
    problem6()
