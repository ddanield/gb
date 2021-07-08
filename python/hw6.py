from time import sleep


# problem1
class TrafficLight:
    STATES = {
        'red': 'yellow',
        'yellow': 'green',
        'green': 'red',
    }
    DELAY = {
        'red': 7,
        'yellow': 2,
        'green': 5,
    }

    def __init__(self, color):
        if color not in self.STATES:
            raise Exception(f'Cannot set state to {color}')
        self.__color = color

    def running(self, new_color):
        if self.STATES.get(self.__color) != new_color:
            raise Exception(f'Cannot change state from {self.__color} to {new_color}')
        self.__color = new_color
        print(f'Running {new_color}')
        sleep(self.DELAY.get(new_color))


# problem2
class Road:
    def __init__(self, length, width):
        self.__length = float(length)
        self.__width = float(width)

    def calc(self, weight, thickness):
        return self.__length * self.__width * float(weight) * float(thickness)


# problem3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        if not isinstance(income, dict) \
                or not isinstance(income.get('wage'), int) \
                or not isinstance(income.get('bonus'), int):
            raise Exception('Income must be a dict with wage, bonus keys with int values')
        self.__income = income

    def get_total_income(self):
        return self.__income.get('wage') + self.__income.get('bonus')


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'


# problem4
class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Here goes! {self.name}')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print('Stop!')
        self.show_speed()

    def show_speed(self):
        print(f'Speed: {self.speed}')

    @staticmethod
    def turn(direction):
        print(f'Turn {direction}')


class TownCar(Car):
    MAX_SPEED = 60

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print('Warning! You drive too fast')
        super().show_speed()


class WorkCar(Car):
    MAX_SPEED = 40


class PoliceCar(Car):
    MAX_SPEED = 1080000000

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_police = True


# problem5
class Stationery:
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    TITLE = 'Ручка'

    def draw(self):
        print(f'Используем инструмент "{self.TITLE}"')


class Pencil(Pen):
    TITLE = 'Карандаш'


class Handle(Pen):
    TITLE = 'Маркер'


if __name__ == '__main__':
    # problem1
    traffic_light = TrafficLight('red')
    traffic_light.running('yellow')
    traffic_light.running('green')

    # Error!
    traffic_light.running('yellow')
    traffic_light.running('grey')

    # problem2
    road = Road(length=5000, width=20)
    print('Result:', road.calc(weight=25, thickness=0.05))

    # problem3
    position = Position('Masha', 'Petrova', 'Programmer', {'wage': 200, 'bonus': 50})
    print(position.get_full_name())
    print(position.get_total_income())

    # Error!
    Position('Masha', 'Petrova', 'Programmer', 100)
    Position('Masha', 'Petrova', 'Programmer', {'wage': 100})

    # problem4
    town_car = TownCar(speed=65, color='Green', name='Zhiguli')
    town_car.go()
    town_car.show_speed()
    town_car.turn('left')
    town_car.stop()

    work_car = WorkCar(speed=30, color='White', name='PAZ-3205')
    work_car.go()
    work_car.show_speed()
    work_car.stop()

    police_car = PoliceCar(speed=120, color='Black', name='BMW')
    police_car.go()
    police_car.go()
    police_car.go()

    # problem5
    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
