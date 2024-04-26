class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound")



lion = Animal("lion", "roar")
dog = Animal("dog", "bark")
cat = Animal("cat", "meow")


lion.make_sound()
dog.make_sound()
cat.make_sound()