class Microwave:
    def __init__(self, brand:str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    # methods
    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off.')
        else:
            print(f'Microwave ({self.brand}) is already turned off.')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds.')
        else:
            print(f'You need to turned on your microwave before run.')

    # dunder methods
    def __add__(self, other):
        return f'{self.brand} + {other.brand}'
    
    def __mul__(self, other):
        return f'{self.brand} * {other.brand}'
    
    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating}))'
    
    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'

smeg: Microwave = Microwave(brand='Smeg', power_rating='B') # With Type annotation
# smeg.turn_on()
# smeg.run(30)
# smeg.turn_off()
# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)

bosch: Microwave = Microwave(brand='Bosch', power_rating='C') 
# bosch.turn_on()
# bosch.run(30)
# bosch.turn_off()
# print(bosch)
# print(bosch.brand)
# print(bosch.power_rating)

print(smeg + bosch)
print(smeg * bosch)
print(smeg)
print(bosch)
print(repr(smeg))
print(repr(bosch))