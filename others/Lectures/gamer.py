class Player:

    def __init__(self, powerlevel: int, power_ups: list, strength: int, stamina: str , name: str):
        self.powerlevel = powerlevel
        self.power_ups = power_ups
        self.strength = strength
        self.stamina = stamina
        self.name = name 

    def set_power_level(self, power):
        self.powerlevel = self.powerlevel + power
        return self

new_player = Player()