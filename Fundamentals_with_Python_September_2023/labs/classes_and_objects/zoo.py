class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {count_of_animals}"
        elif species == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {count_of_animals}"
        elif species == "bird":
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {count_of_animals}"


name_of_the_zoo = input()
zoo_object = Zoo(name_of_the_zoo)
count_of_animals = int(input())
for animal in range(count_of_animals):
    species, name = input().split()
    zoo_object.add_animal(species, name)

searched_species = input()
print(zoo_object.get_info(searched_species))