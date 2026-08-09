class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

print("Initial Attributes: " + whiskers.name + " (" + whiskers.species + ") - Hunger: " + str(whiskers.hunger) + ", Energy: " + str(whiskers.energy))

whiskers.hunger = whiskers.hunger - 3
whiskers.energy = whiskers.energy + 2
# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

print("Modified Attributes: " + whiskers.name + " (" + whiskers.species + ") - Hunger: " + str(whiskers.hunger) + ", Energy: " + str(whiskers.energy))

