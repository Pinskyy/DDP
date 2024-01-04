# Class Animal
class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

# Badak
class Rhino(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "Rumput", habitat, "Vivipar")

    def attack(self):
        print(f"{self.name} sedang menyerang dengan cara mengejar lawannya!")

# Ikan
class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "Plankton", habitat, "Ovipar")

    def renang(self):
        print(f"{self.name} sedang berenang di dalam air.")

# Ular
class Snake(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "Hewan kecil", habitat, "Ovipar")

    def merayap(self):
        print(f"{self.name} sedang merayap di tanah.")

rhino = Rhino("Badak Sumatra", "Hutan")
fish = Fish("Ikan Koi", "Kolam")
snake = Snake("Ular Sanca", "Lembah")

print(f"{rhino.name} hidup di {rhino.habitat}, memakan {rhino.food}, dan berkembang biak secara {rhino.reproduction}.")
rhino.attack()

print(f"{fish.name} hidup di {fish.habitat}, memakan {fish.food}, dan berkembang biak secara {fish.reproduction}.")
fish.renang()

print(f"{snake.name} hidup di {snake.habitat}, memakan {snake.food}, dan berkembang biak secara {snake.reproduction}.")
snake.merayap()