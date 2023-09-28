import threading

# print("Hello world!")
# time.sleep(5)
# 1/0
# print(2+3)

# abc = 123

# datatypes
# int = 1
# string = "abc"
# float = 2.5
# bool = True/False

#primitive data-types
# tuple = (1,2,3)
# list = [1,2,3,4]   [[1,2], 3, [4,5,6], 7]
# set = {1,2,3}
# dict = {'1': 1, '2': 'abc'}


# li1 = [1,2,3]
# li2 = [4,5,6]

# li3 = [1,2,3,4,5,6]

# li3 = li1+li2
# print(li3)

# li4 = [1,2,3,4]
# print(li1)
# li1.append(3)
# li1.append(100)
# print(li1)

# li1.pop()
# print(li1)

# li4 = [4,5,6,7,8,9,10]

# li4[:4]
#  print(li4)

# pycharm, atom

# print(li4[::-2])

# dt = {'1': 1, '2': 'abc', '3': 'xyz', '4': 'lmn'}

# # dt['3'] = 'xyz'

# print(dt.pop('4'))
# print(dt)

# dictionary operatons - https://www.w3schools.com/python/python_ref_dictionary.asp
# list operations - https://www.educba.com/list-operations-in-python/#:~:text=A%20few%20of%20the%20basic,()%2C%20clear()%2C%20etc.

# types of comments
# 2 statements to print 123 nd 456
"""kjhkjh
print(123)
print(456)
"""

# def xyz():
#     """ creating a li and looping it from 1,10
#     the li is append with the objects and return the list itself
#     """
#     li = []
#     for i in range(10):
#         li.append(i)
#         print(i)
#     return li

# concatination
# first_name = 'john'
# last_name = 'doe'

# full_name = first_name + last_name
# print(full_name)

# Functions in python
# def animals_in_forest():
#     li = ['lion', 'tiger', 'giraffe']
#     li1 = []
#     for i in li:
#         print(i + 'a')
#         li1.append(i + 'a')
#     return 'abc'
# a = animals_in_forest()
# print(a)

# classes in python
class AnimalsInForest:
    def _init_(self, name, legs):
        self.name = name
        self.legs = legs
        

class PetAnimals:
    def cat(self, name):
        self.name = name
        print(self.name)

a = AnimalsInForest("lion", 4)
print(a.legs)


b = PetAnimals()

b.cat('cat')

# pep8 - guidelines