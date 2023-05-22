#------------------ 1.2 ------------------
class User:
    nickname: str
    money: int = 30000
    fraction: str = ""
    rang: int = 0
    spaceships: list[Starship] = ["Sidewinder"]
    achievements: list[Achievement] = []

class Starship:
    name: str
    type_ship: str
    color: str
    price: int
    equipments: list[Equipment]
    fuel: int
    energy: int

class Fraction:
    name: str
    capital: str
    planets: list[Planet]
    language: str
    currency: str
    population: int
    established: int

#------------------ 1.3 ------------------

lei = User()

lei.nickname="Lei"
lei.fraction="Independent"


marco = lei
marco.nickname = "Marco"


print("Class lei nickname: ", lei.nickname)
print("Class marco nickname: ", marco.nickname)



