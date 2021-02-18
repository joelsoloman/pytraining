#Question 1 - Iterator

class UserDefined:
    
    def __init__(self, word):
        self.word = word
        self.index = -2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 2
        if self.index >= len(self.word):
            raise StopIteration
        if self.index % 2 == 0:
            return self.word[self.index]

example = UserDefined("Banana")
it = iter(example)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

#Question 2 - CSV
import csv

with open('Data.csv','w') as file:
    newFile = csv.writer(file)
    newFile.writerow(['Name','Experience'])
    newFile.writerow(['Harry Potter','8 Years'])
    newFile.writerow(['Bruce Wayne','12 Years'])
    newFile.writerow(['John Doe','4 Years']) 

#Question 3 - Roaming through directory

import os
for (_, _, files) in os.walk("E:\Python works\Training Practice\PracticePrograms_Day4_Joel"):
    for file in files:
        if '.py' in file:
            print(file)

#Question 4 - Standard lib || Command Line Arguments

import sys
cmdArgs = sys.argv
print(cmdArgs)

#Question 5 - Guessing game with Exceptions

class CustomException(Exception):
    def  __init__(self, arg):
        self.args = {arg}
        
def init_guess():
    return int(input("Guess again:"))

guess = int(input("Enter your Guess:"))
target = 10
attempts = 0

for attempts in range(2):
    if guess>target:
        print("Guess is Higher than the target")
        guess = init_guess()
    elif guess<target:
        print("Guess is Lower than the target")
        guess = init_guess()
    else:
        print("Guess is Correct")
        break                               #If correct within 2 tries else is not invoked
    attempts += 1
else:                                      
    if guess == target:
        print("Success")
    else:
       raise CustomException("Out of tries")

#Question 6 - Type and Value Errors

try:
    int_object = int(input("Enter a Number:")) #Anything else from an integer will trigger a ValueError
    print(int_object + " Some String")  #An integer cannot be concatinated Thus triggering a TypeError
except ValueError:
    print("Value Error Triggered")
except TypeError:
    print("Type Error Triggered")
except:
    print("Other Errors")

#Question 7 - Index and Key Errors

try:
    d = {'name':'aaa','age':18,'email':'abc@g.com'}
    print(d['address'])
except KeyError:
    print("Key Error Triggered")

try:
    list = [1,2,3]
    print(list[3])
except IndexError:
    print("Index Error Triggered")

#Extra Mile

for (_, _, files) in os.walk("E:\Python works\Training Practice\PracticePrograms_Day4_Joel"):
    it = iter(files)
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    