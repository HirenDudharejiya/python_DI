# classes in python

#     """This will accept 4 paramters
#     :params: name - "string: Takes the name of animal
#     :params: legs - "int" Takes the number of legs
#     :params: tail - "Boolean" If tail exists
#     :params: place - "string: Where animal resides
#     """
class AnimalsInForest:
    def _init_(self, name, legs, tail, place):
        self.name = name
        self.legs = legs
        self.tail = tail
        self.place = place

a = AnimalsInForest('Dog', 4, True, 'India')
print(a.name)

# b = AnimalsInForest('Cat', '4', True, 'USA')
# print(b.place)

# class PetAnimals:
#     def cat(self, name):
#         self.name = name
#         print(self.name) 

#     def dog(self, breed, height):
#         self.breed = breed
#         self.height = height
#         print(self.breed, self.height)
# a = PetAnimals()
# a.dog('labrador', '2"0')

# class Base:
#     def _init_(self):
#         print("iam in base class")

# class Child(Base):
#     def _init_(self):
#         print("Iam in child class", Base())

# child = Child()
# b = PetAnimals()

# b.cat('cat')

# pep8 - guidelines

# Package installer - pip for python
# https://pip.pypa.io/en/stable/cli/pip_install/

#arithematic operation
# https://www.w3schools.com/python/python_operators.asp
# print((2.5+3)*7.5)

# print('5' + 5)
# import math
# import random
# print(random.randint(1,10))

# logical operations
# a = 123
# print(2 >= -2)

#assignment operators
# i = 1
# i += 3
# print(i)

# print(20/3)