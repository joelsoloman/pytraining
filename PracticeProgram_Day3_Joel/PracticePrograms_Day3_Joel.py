#1. Dictionaries

nums = [1,2,3]
squares = {num : num**2 for num in nums}            #1.a
print(squares)
squaresList = [value for value in squares.values()] #1.b
print(squaresList)

#2. set comprehension

setCompList = [1, 2, 5, 2, 3, 1, 4, 5]
resultSet = {element**2 for element in setCompList}
print(resultSet)

#3. Tuples

givenListOfTuple = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
properBalancesDictionary = {name : balance for (name, balance, min) in givenListOfTuple if min < balance}           #3.a
print(properBalancesDictionary)

balancesSet = {element for (_, element, _) in givenListOfTuple}                                                     #3.b
print(balancesSet)

accountHolderList = [holder for (holder, _, _) in givenListOfTuple]                                                 #3.c
print(accountHolderList)

remainingBalanceDictionary = {name : min-balance for (name, balance, min) in givenListOfTuple if min > balance}     #3.d
print(remainingBalanceDictionary)

balanceAboveZeroList = [(name,balance) for (name, balance, _) in givenListOfTuple if balance > 0]                   #3.e
print(balanceAboveZeroList)

#4. Class

class Developer:

    def __init__(self):
        self.languages = []
    
    def code(self,language):
        if(language not in self.languages):
            self.languages.append(language)
        else:
            print(f"code in {language}")

    def resume(self):
        print(self.languages)

employee1 = Developer()
employee1.code("C")
employee1.code("Java")                  #4.a
employee1.resume()                      #4.b

class SrDeveloper(Developer):

    def __init__(self):
        self.reviews = []
        Developer.__init__(self)

    def review(self,review):            #4.c
        if(len(self.reviews)<len(self.languages)):
            self.reviews.append(review)
    
    def viewReviews(self):
        print(self.reviews)
        
employee2 = SrDeveloper()
employee2.code("Java")
employee2.review("Good")

class TechLead(SrDeveloper):

    def __init__(self):
        SrDeveloper.__init__(self)
    
    def design(self):                       #4.d
        print("Design called by TechLead")

employee3 = TechLead();
employee3.code("Java")
employee3.code("C")
employee3.resume()
employee3.review("Good")
employee3.review("Excellent")
employee3.review("Average") #Doesn't get appended as the Code size limits the Reviews size
employee3.viewReviews()
employee3.design()          #Object of Subclass calling all it's parent's functions

#5. Factorial of List

from math import factorial

class Factorial:

    def __init__(self):
        self.result = []
    
    def compFact(self,numbers):
        for number in numbers:
            self.result.append(factorial(number))
        return self.result

newObject = Factorial()
print(newObject.compFact([1,2,3,4,5]))

#6. Imports

from Day3_ImportModule import printFuntion as moduleFunc
moduleFunc()

#7. Extras

TestObject = "This is a String"
print(TestObject.__str__())
print(TestObject.__repr__())
print(TestObject.__len__())
TestNumber = 25.652
print(TestNumber.__int__())
print(TestNumber.__float__())
print(TestNumber.__round__())