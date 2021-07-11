from collections import defaultdict
from datetime import datetime


class MyDate:
    def __init__(self, date_string):
        self.date_string = date_string

    def __str__(self):
        return self.date_string

    @classmethod
    def get_numbers(cls, obj):
        date = cls.validate(obj)
        return date.day, date.month, date.year

    @staticmethod
    def validate(obj):
        try:
            return datetime.strptime(obj.date_string, '%d-%m-%Y')
        except ValueError as e:
            print(f'Expected data in format dd-mm-YYYY, got {obj}')
            raise e


class MyCustomException(Exception):
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message


class Warehouse:
    def __init__(self):
        self.warehouses = dict()

    def add_device(self, warehouse, device, count):
        if not isinstance(device, OfficeDevice):
            raise Exception('Error! Device must instantiate class OfficeDevice')
        try:
            count = int(count)
        except ValueError as e:
            print('Error! Cannot parse device count')
            raise e

        if warehouse not in self.warehouses:
            self.warehouses[warehouse] = defaultdict(int)
        self.warehouses[warehouse][device] += count

    def print_report_device_type(self, device_type):
        if not issubclass(device_type, OfficeDevice):
            raise Exception('Error! Device type must be subclass of OfficeDevice')

        for warehouse_name, warehouse in self.warehouses.items():
            for device, count in warehouse.items():
                if device.device_type == device_type:
                    print(f'{warehouse_name}, {device}, {count}')

    def print_report_warehouse(self, warehouse_name):
        if warehouse_name not in self.warehouses:
            raise Exception(f'Cannot find warehouse {warehouse_name}')

        warehouse = self.warehouses[warehouse_name]
        for device, count in warehouse.items():
            print(f'{warehouse_name}, {device}, {count}')


class OfficeDevice:
    def __init__(self, name, device_type=None):
        self.name = name
        self.device_type = device_type


class Printer(OfficeDevice):
    def __init__(self, name, printer_type=None, page_format=None):
        super().__init__(name, device_type=self.__class__)
        self.printer_type = printer_type
        self.page_format = page_format

    def __str__(self):
        return f'{self.device_type.__name__}: {self.name} {self.printer_type} {self.page_format}'


class Scanner(OfficeDevice):
    def __init__(self, name, page_format=None, resolution=None):
        super().__init__(name, device_type=self.__class__)
        self.page_format = page_format
        self.resolution = resolution

    def __str__(self):
        return f'{self.device_type.__name__}: {self.name} {self.page_format} {self.resolution}'


def problem1():
    date_1 = MyDate('10-07-2021')
    print(MyDate.validate(date_1))
    print(MyDate.get_numbers(date_1))

    # Error
    # date_2 = MyDate('asd')
    # print(MyDate.validate(date_2))
    # print(MyDate.get_numbers(date_2))
    # date_3 = MyDate('2021-07-10')
    # print(MyDate.validate(date_3))
    # print(MyDate.get_numbers(date_3))


def problem2():
    while True:
        try:
            a, b = map(int, input('Enter two numbers: ').split())
            if b == 0:
                raise MyCustomException('Error! Division by zero')
            print('Result:', a / b)
            break
        except ValueError:
            print('Error! Cannot parse input numbers')
        except MyCustomException as e:
            print(e)


def problem3():
    elements = []
    while True:
        elem = input().strip()
        if elem.lower() == 'stop':
            break
        try:
            found_comma = False
            for idx, letter in enumerate(elem):
                if letter == '-':
                    if idx != 0:
                        raise MyCustomException
                elif letter == '.':
                    if found_comma:
                        raise MyCustomException
                    found_comma = True
                elif not letter.isdigit():
                    raise MyCustomException
            if found_comma:
                elements.append(float(elem))
            else:
                elements.append(int(elem))
        except MyCustomException:
            print(f'Error! Cannot parse input number {elem}')

        print(f'Current elements: {elements}')


def problem4_5_6():
    warehouse = Warehouse()
    warehouse.add_device('Warehouse 1', Printer('Kyocera P2335dn', 'Laser', 'A4'), 10)
    warehouse.add_device('Warehouse 1', Printer('Xerox Phaser 3020BI', 'Laser', 'A4'), 5)
    warehouse.add_device('Warehouse 1', Scanner('Canon CanoScan LiDE 300', 'A4', '2400dpi'), '5')

    warehouse.add_device('Warehouse 2', Printer('Kyocera P2335dn', 'Laser', 'A4'), '5')
    warehouse.add_device('Warehouse 2', Scanner('Canon CanoScan LiDE 300', 'A4', '2400dpi'), 5)

    print('Report for Scanners')
    warehouse.print_report_device_type(Scanner)
    print('Report for Printers')
    warehouse.print_report_device_type(Printer)
    print('Report for Warehouse 1')
    warehouse.print_report_warehouse('Warehouse 1')
    print('Report for Warehouse 2')
    warehouse.print_report_warehouse('Warehouse 2')

    # Error
    # warehouse.add_device('Warehouse 1', 123, 10)
    # warehouse.add_device('Warehouse 1', Scanner('Canon CanoScan LiDE 300', 'A4', '2400dpi'), 'asd')
    # warehouse.print_report_device_type(object)
    # warehouse.print_report_device_type('asd')
    # warehouse.print_report_warehouse('Warehouse 3')


if __name__ == '__main__':
    problem1()
    problem2()
    problem3()
    problem4_5_6()
