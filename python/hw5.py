import os
import re
import statistics

DATA_FOLDER = 'data'


def problem1():
    filename = os.path.join(DATA_FOLDER, 'problem1.txt')
    with open(filename, 'w', encoding='utf8') as f:
        while True:
            line = input().strip()
            if not line:
                break
            print(line, file=f)


def problem2():
    filename = os.path.join(DATA_FOLDER, 'problem2.txt')
    with open(filename, 'r', encoding='utf8') as f:
        lines_count = 0
        for line in f:
            line = line.strip()
            print(line, '-', len(line))
            lines_count += 1
        print('Total lines:', lines_count)


def problem3():
    filename = os.path.join(DATA_FOLDER, 'problem3.txt')
    with open(filename, 'r', encoding='utf8') as f:
        salary_list = []
        salary_less_than_20_names = []
        for line in f:
            name, salary = line.split('-')
            salary = int(salary)
            if salary < 20:
                salary_less_than_20_names.append(name.strip())
            salary_list.append(salary)

    if salary_less_than_20_names:
        print('Colleagues with salary less than 20:')
        print('\n'.join(salary_less_than_20_names))

    print('Average salary:', statistics.mean(salary_list))


def problem4():
    numerals = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
    }

    filename = os.path.join(DATA_FOLDER, 'problem4.txt')
    with open(filename, 'r', encoding='utf8') as f:
        lines = f.read()
        lines = lines.strip().split('\n\n')
        for idx, sub_lines in enumerate(lines):
            filename_out = os.path.join(DATA_FOLDER, f'problem4_out_{idx + 1}.txt')
            with open(filename_out, 'w', encoding='utf8') as f_out:
                for line in sub_lines.split('\n'):
                    number_str, number = line.split('-')
                    print(numerals.get(number_str.strip()), '-', number.strip(), file=f_out)


def problem5():
    filename = os.path.join(DATA_FOLDER, 'problem5.txt')
    with open(filename, 'w', encoding='utf8') as f:
        line = input().strip()
        print(line, file=f)

    with open(filename, 'r', encoding='utf8') as f:
        lines = f.read().split()
        print('Result:', sum(map(int, lines)))


def problem6():
    filename = os.path.join(DATA_FOLDER, 'problem6.txt')
    subjects_dict = {}
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            subject, hours = line.split(':')
            hours = re.findall(r'\b\d+\b', hours)
            subjects_dict[subject] = sum(map(int, hours))

    print(f'Result:')
    print(subjects_dict)


def problem7():
    import json

    filename = os.path.join(DATA_FOLDER, 'problem7.txt')
    firms_dict = {}
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            firm, ownership, gain, costs = line.split()
            firms_dict[firm] = int(gain) - int(costs)
    average_profit = {'average_profit': statistics.mean([p for p in firms_dict.values() if p > 0])}

    filename_out = os.path.join(DATA_FOLDER, 'problem7.json')
    with open(filename_out, 'w') as f:
        json.dump([firms_dict, average_profit], f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
    problem7()
