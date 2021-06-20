def problem1():
    def division(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

    a, b = map(int, input().split())
    print(f'Result: {division(a, b)}')


def problem2():
    def print_user_data(first_name, last_name, birth_year, city, email, phone):
        print(f'First name: {first_name}, Last name: {last_name}, Birth year: {birth_year}, '
              f'City: {city}, Email: {email}, Phone: {phone}')

    print_user_data(
        first_name='Maria',
        last_name='Ivanova',
        birth_year=1992,
        city='Moscow',
        email='maria.ivanova@example.com',
        phone=71234567891
    )


def problem3():
    def my_func(a, b, c):
        if a <= b:
            if a <= c:
                return b + c
            else:
                return a + b
        else:
            if b <= c:
                return a + c
            else:
                return a + b

    a, b, c = map(int, input('Enter three numbers: ').split())
    print(f'Result: {my_func(a, b, c)}')


def problem4():
    def my_func(x, y):
        if y == 0:
            return 1
        res = 1
        for _ in range(abs(y)):
            res *= x
        if y < 0:
            res = 1 / res
        return res

    x, y = map(int, input('Enter two numbers: ').split())
    print(f'Result: {my_func(x, y)}')


def problem5():
    current_sum = 0
    while True:
        lines = input().split()
        if lines and lines[-1] == 's':
            break
        lines = map(int, lines)
        current_sum += sum(lines)
        print(f'Current sum: {current_sum}')


def problem6():
    def int_func(s):
        if s:
            code_a = ord('a')
            code_z = ord('z')
            code_diff = ord('A') - code_a
            code_first_letter = ord(s[0])
            if code_a <= code_first_letter <= code_z:
                s = chr(code_first_letter + code_diff) + s[1:]

        return s

    lines = input().split()

    print(f'Result: {" ".join(map(int_func, lines))}')


if __name__ == '__main__':
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
