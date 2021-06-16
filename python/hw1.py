def problem1():
    a = b = 1
    print(f'a={a}, b={b}')

    input_string = input('Enter a string: ')
    input_int = int(input('Enter an integer: '))

    print(input_string, input_int)


def problem2():
    seconds = int(input('Enter seconds number: '))
    minutes = seconds // 60
    hours = seconds // 3600
    print('Time: {hours:0>2}:{minutes:0>2}:{seconds:0>2}'.format(
        hours=hours, minutes=minutes % 60, seconds=seconds % 60
    ))


def problem3():
    n = input('Enter a number: ')
    print(f'Result: {int(n) + int(n * 2) + int(n * 3)}')


def problem4():
    n = int(input('Enter a number: '))
    max_digit = 0
    while n != 0:
        if (digit := n % 10) > max_digit:
            max_digit = digit
        n //= 10
    print(f'Result: {max_digit}')


def problem5():
    receipts = int(input('Enter the receipts: '))
    costs = int(input('Enter the costs: '))
    if receipts > costs:
        print('Profit!')

        profit = receipts - costs
        print(f'Profit efficiency: {profit / receipts}')

        employees = int(input('Enter the number of employees: '))
        print(f'Profit per employee: {profit / employees}')
    elif costs > receipts:
        print('Loss')
    else:
        print('Payback')


def problem6():
    a = int(input('Enter current result in kilometers: '))
    b = int(input('Enter desired result in kilometers: '))
    percents = 10

    days = 1
    print(f'{days} day: {a} kilometers')
    while a < b:
        days += 1
        a += a / percents
        print(f'{days} day: {a:.2f} kilometers')
    print(f'Result: {days}')


if __name__ == '__main__':
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
