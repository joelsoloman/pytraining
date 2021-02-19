#Timeit Decorator

import timeit
from functools import wraps
def timer(func):
    @wraps(func)
    def inner(*args):
        strt = timeit.default_timer()
        func(*args)
        stop = timeit.default_timer() - strt
        print(stop)
    return inner

@timer
def something(Eg):
    print(f"This is {Eg}")

something("Blahblah")

#Generator as an Iterator

def jump_str(word):
    for i in range(0,len(word),2):
        yield word[i]

for char in jump_str("Python"):
    print(char)

#Overwriting Dunder Methods

class MyClass:

    def __init__(self,myWord):
        self.myWord = myWord
    
    def __str__(self):
        print(f"{self.myWord} is the Word you've Given")
    
    def __add__(self,new):
        self.myWord = self.myWord+' '+new
        print(self.myWord)

object = MyClass("Python")
object.__str__()
object.__add__('Programs')
object.__add__('Are')
object.__add__('Awesome')