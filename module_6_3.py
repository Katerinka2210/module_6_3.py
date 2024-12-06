import random
class Animal:
    live = True # жизнь
    sound = None # звук
    _DEGREE_OF_DANGER = 0    # степень опасности существа, изначально 0
    def __init__(self, speed):  # cords - координаты в пространстве, изначально 0
        self._cords = [0, 0, 0]  # координаты объекта
        self.speed = speed #скорость объекта

    def move(self, dx, dy, dz):
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed
        if z < 0:
            print("It's too deep, i can't dive :(") # слишком глубоко, я не могу нырнуть
        else:
            self._cords = [x, y, z]  # как прописать, что координаты меняются в том же порядке, где множетелем будет speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")  # извини, я миролюбивый
        else:
            print("Be careful, i'm attacking you 0_0")  # будь осторожен, я нападаю

    def speak(self):
        print(f'{self.sound}')


class Bird(Animal):    # класс птиц
    beak = True  # наличие клюва
    def lay_eggs(self):
        random_number = random.randint(1, 4)
        print(f"Here are(is) {random_number} eggs for you")

class AquaticAnimal(Animal):  # класс, описывающий плавающего жевотного
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dive_z = abs(dz) // 2 * self.speed  # взяли значение Dz по модулю и уменьшили скорость движения при нырянии в 2 раза
        self._cords[2] -= dive_z # уменьшили "-=" на переменную dive_z


class PoisonousAnimal(Animal): # класс ядовитых животных
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):  # класс описывающий утконоса
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)




db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()