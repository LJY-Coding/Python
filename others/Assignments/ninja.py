class Ninja:
    def __init__(self, data):
        self.f_name = data["first_name"]
        self.l_name = data["last_name"]
        self.pet = data["pet"]
        self.treats = data["treats"]
        self.pet_food = data["pet_food"]

    def walk(self):
        pass

    def feed(self):
        pass

    def bathe(self):
        pass


class Pet:
    def __init__(self, data_pet):
        self.name = data_pet["name"]
        self.type = data_pet["types"]
        self.tricks = data_pet["tricks"]
        self.health = data_pet["health"]
        self.energy = data_pet["energy"]

    def sleep(self):
        pass

    def eat(self):
        pass

    def play(self):
        pass

    def noise(self):
        pass