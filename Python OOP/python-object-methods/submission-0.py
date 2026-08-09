class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger -= 1
        print("Fluffy has been fed.")
        print("Fluffy's hunger level: " + str(self.hunger))

# Create a pet
my_pet = Pet("Fluffy")

for i in range(3):
    my_pet.feed()