#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self
    
    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog("Fido")
fido.showing_self()
print(fido.name)
fido.get_adopted("Sophie")
print(fido.owner)
# print(fido.favorite_toy)

snoopy = Dog("Snoopy", "Tennis Ball")
# print(snoopy.favorite_toy)
print(snoopy.name)