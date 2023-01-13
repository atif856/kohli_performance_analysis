class SuperHero():
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def get_SuperPower(self):
        print(f"\nI am {self.name} and power is {self.superpower}\n")

ironman = SuperHero(name="Ironman", superpower="suit")
print(ironman.name)
print(ironman.superpower)
ironman.get_SuperPower()
        
thor = SuperHero(name="Thor", superpower="Hammer")
print(thor.name)
print(thor.superpower)
thor.get_SuperPower()

