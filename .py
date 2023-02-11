class Car:
    # fields (atribute)
    make = 'Dacia'
    model = None
    year = 2022
    color = None

    # constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # methods:
    def accelerate(self):
        print('Vrumm VRUUM')

    def stop(slef):
        print('STOP!')


car1 = Car('Duster', 'white')
car2 = Car('logan', 'blue')
print(car1.make)
print(car1.model)
print(car1.color)
car1 = Car('Duster', 'white')  # initializam obiecte de tip car
car2 = Car('logan', 'blue')  # car 2 este instanta a clasei car
print(car1.make)  # dupa avem acces la fields
print(car2.make)
car1.model = 'Duster'  # pitem suprascrie valori
car2.model = 'Logan'
car1.accelerate()  # dupa avem acces la methods
car1.stop()
