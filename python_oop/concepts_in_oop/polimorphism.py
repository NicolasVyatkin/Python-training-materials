﻿# перевантаження або перевизначення методу

class Car:
    def __init__(self, name):
        self.__name_speed_dict = {
            "Mercedes": 250,
            "BMW": 300,
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self.__name_speed_dict.get(name, 0)

    def distance_time_on_max_speed(self, distince):
        if not self._max_speed:
            print("No speed param specified")
            return 0
        return distince / self._max_speed


car_a = Car(name="BMW")
car_b = Car(name="Mercedes")
print(car_a.distance_time_on_max_speed(distince=167))
print(car_b.distance_time_on_max_speed(distince=167))
print('#################')
######################################################


class Animal:
    def __init__(self, name):
        self.name = name

    def voise(self):
        if self.name == 'dog':
            print('Bark!!!')
        elif self.name == 'cat':
            print('Meow!!!')
        else:
            print('Silence...')


cat = Animal(name='cat')
dog = Animal(name='dog')
veloseraptor = Animal(name='veloseraptor')
cat.voise()
dog.voise()
veloseraptor.voise()
print('#################')
######################################################


class Multiplayer:
    def __init__(self, multiplayer):
        self._multiplayer = multiplayer

    def multiply(self, variable):
        return variable * self._multiplayer


mult_inst = Multiplayer(3)
print(mult_inst.multiply('hello!!! '))
print(mult_inst.multiply(4))
print('#################')
######################################################
