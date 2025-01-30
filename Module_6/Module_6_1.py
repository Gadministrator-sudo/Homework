
class Animal:                                           # Родительский класс
    alive = True                                        # атрибут Живой
    fed = False                                         # атрибут Накормленный
    def __init__(self,name):                            # Конструктор объекта класса
        self.name = name

class Plant:                                            # Родительский класс
    edible = False                                      # атрибут Съедобность
    def __init__(self,name):
        self.name = name

#______________________________________________________________________________________________#

class Mammal(Animal):                                   # Класс наследующий классу Animal - Травоядные

    def eat(self, food):                                # Метод
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):                                          # Класс наследующий классу Animal - Хищники
    def eat(self, food):
        if food.edible:
            print(f'{self.name} сьел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ #

class Flower(Plant):                                    # Класс наследующий классу Plant - цветы
    pass

class Fruit(Plant):
    edible = True

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)