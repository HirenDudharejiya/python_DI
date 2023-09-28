# if else, and if elif else
# a = ''  # None, "", {}, [], False, 0
# b = False
# if a:
#     print("Value of a is True")
#     print("2nd statement")
#     if b:
#         print("value of b is 123")
# else:
#     print("Value of a is False")
#     if b:
#         print("value of b is 123")
# c = 123
# if a:
#     print("Value of a is True")
# elif b:
#     print("Value of b is True")
# elif c:
#     print("Value of c is True")
# else:
#     print("Else statement")
# a = 6
# b = 9
# if a==b and 2==2:
#     print('Both conditions satisfies')
# elif True:
#     print('Inside elif condition')

# for loop
# li = [0,1,2,3,4,5]
# for x in li:
#     if x%2 == 0:
#         print(list(x))
        # print()
#     else:
#         print(int(x) + " is a odd number")

# list comprehension
# li1 = [x if x%2 == 0 else x for x in li]
# [x for x in li if x%2==0]

# dict comprehension
# d = {'abc': 123, 'xyz': 890}
# d1 = {k: v for (k,v) in d.items() if k=='abc'}
# print(d1)

# d = {'first_name': 123, 'last_name': 890, 'age': 18, 'address': "Lost street"}
# d1={k:v for (k,v) in d.items() if k=='abc'}
# print(d1)

# for x in d:
#     if x == 'age':
#         if d['age'] >= 18:
#             print('The person is above or equal to 18')
#         else:
#             print('The person is below 18')

# f strings and .format, inline variable concatination
# abc = 123
# xyz = 789
# s = f"The number provided is: {abc+xyz}"
# s1 = "The number provided is: {}".format(abc+xyz)
# print(s1)


# lambda functions
# def abc(a):
#     return a+2

# x = abc(2)

# x= lambda a: a+2
# print(x(2))

# generators in python
# li = [1,2,3,4,5]
# def abc():
#     for x in li:
#         yield x

# x = abc()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# while loop
# li1 = [1,2,3,4,5,6,7,8,9]
# x = 8
# while True:
#     if x <= 6:
#         print(x)
#         break
#     else:
#         print(x)

# Error handling try except finally
# try:
#     1/0
#     print('This is a try statement')
        
# except ZeroDivisionError as e:
#     print(f'This is a zerodivision statement: {e}')
# except TypeError as e:
#     print(f'This is a Type error statement: {e}')
# except Exception as e:
#     print(f'This is a except statement: {e}')
# else:
#     print('THis is a try/else statement')
# finally:
#     print('This is a finally statement')

# range in python
# for x in range(5, 103, 5):
#     print(x)

# input() method
# while True:
#     try:
#         a = int(input("Give a number for range: "))
#         print(f"The number given by you is {a}")

#         for x in range(0, a):
#             print(x)
#         break
#     except:
#         print('Please give number.')

# datetime library:  https://docs.python.org/3/library/datetime.html


# import datetime
# age = int(input("Please give your birthyear: "))
# current_year = datetime.datetime.today().strftime('%Y')
# current_year = int(current_year)
# print(f"Your age is: {current_year-age}")

# Variable scope

# def new_variable():
#     global a 
#     a = 'Variable a inside new_variable function'
#     print(a)
#     return a

# def n1():
#     print('Function n1')

# def n2():
#     print('Function n2')

# def n3():
#     v1 = new_variable()
#     print('Function n3', v1)
#     print(a)

# n3()
# class NewClass:
#     def _init_(self, b, c):
#         self.b = b
#         self.c = c

#     def variable1(self, e):
#         # b = 'Variable b'
#         print(e)
#         print(self.b)

#     def variable2(self):
#         # c = 'Variable c'
#         print(self.c)

# d = 'Variable d'

# # var = NewClass('Variable b', 'Variable c')
# # var.variable1("Variable e")

# map, filter, reduce
# map(function, iterable) 
# li = [1,2,3,4,5]

# li1 = list(map(lambda x: x+2, li))
# print(li1)

# filter(function, iterable)
# li2 = list(filter(lambda x: x%2 == 0, li))
# print(li2)

# reduce(function, iterable)
# from functools import reduce
# li3 = reduce(lambda x, y: x/y, li)
# print(li3)

# recurssion
# a1 = 1
# def recur(a):
#     if a == 0:
#         pass
#     print(a1)
#     a1 = a * recur(a-1)

# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# fac = recur_factorial(995)
# print(fac)

# Zip function
# d1 = {'first_name': 'John'}
# d2 = {'last_name': 'Doe'}

# l1 = [0,1,2,3,4]
# l2 = [9,8,7,6,5]
# print(list(zip(l2, l1)))

# Enumerate
# l2 = [9,8,7,6,5]
# print(list(enumerate(l2, 10)))

# static method ad classmethod - https://www.geeksforgeeks.org/class-method-vs-static-method-python/
# class Employee:
#     def _init_(self, firstname, lastname) -> None:
#         self.firstname = firstname
#         self.lastname = lastname

#     @staticmethod
#     def fullname(self) -> str:
#         return self.firstname + ' ' + self.lastname
    
#     @classmethod
#     def ctc(cls, salary):
#         return salary*12
# ------------------------------------------------------------------

# Regex - Regular expressions - https://www.w3schools.com/python/python_regex.asp

# ^ - carot - startswith
# $ - dollar - endwith
# ^text*.txt - wildcard 
# import re
# pattern = re('\d{5}([- ]*)\d{6}')

# ph = '03595-259506'

# s = "The rain in Spain"
# a = re.search('\d{5}([- ]*)\d{6}', ph)
# print(a)
