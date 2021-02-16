#1.Improved Guessing game
print('Guessing game \n')

def init_guess():
    return int(input("Guess again:"))

guess = int(input("Enter your Guess:"))
target = 10
attempts = 0

while attempts < 2:
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
else:                                       #4.Demonsrating Else clause for While loop
    if guess != target:
        print("Your Attempts are over")
    else:
        print("Guess is Correct on Last try")

#2.Printing elements along with position
print('\nPrinting Elements of List along with enum \n')

names = ['Sarah','Joe','Tiara','Michael']
for index,name in enumerate(names):
    print(f"{index}. {name}")

#3.Looping over Dictionary
print('\nLooping over a Dictionary \n')

d = {1:'Biriyani',2:'Fired rice',3:'Noodles'}
for key, value in d.items():
    print(f'{value} belongs to {key}')

#5.Add function
print('\nFunction to add two numbers and finding its type \n')

def add(num_1, num_2):
    """A Function that returns the Sum of two numbers passed to it"""

    print("Type of Arguments is "+str(type(num_1)))
    return num_1+num_2

print(add(1,2))

#6.Function for multiple args
print('\nFunction for Multiple Arguments \n')

def dynamic_args(*args):
    print(f'Count of Args = {len(args)}')
    for item in args:
        print(item)

dynamic_args(1,2,3,4,5)

#7.Function for multiple kwargs
print('\nFunction for Multiple KwArgs \n')

def multi_kwargs(**kwargs):
    print(f'Count of KArgs = {len(kwargs)}')
    for k,v in kwargs.items():
        print(f'{k} -> {v}')

multi_kwargs(name="Mr.ABC",email="abc@gmail.com",phoneNo="1234567890")

#8. Function for Both args and kwargs
print('\nFunction to find the count of Args and KwArgs \n')

def both_count(*args, **kwargs):
    print(f'There are {len(args)} Arg elements and {len(kwargs)} KwArgs elements')

both_count(1,2,3,4,5)
both_count(name="Mr.ABC",email="abc@gmail.com",phoneNo="1234567890")
both_count(1,2,3,4,5,name="Mr.ABC",email="abc@gmail.com",phoneNo="1234567890")

#9. Lambda Expression
print('\nLambda Expression to find the Avg of total 10 and count 2 \n')

avg = lambda t,c : t/c
print(avg(10,2))

#10.Comprehension to get odd no's squares
print('\nList Comprehension to get Odd no\'s squares \n')

given = [1,3,3,4,5,6]
oddSqList = [pow(num,2) for num in given if num%2!=0]
print(oddSqList)


#Bonus Challenge 1 - Get Keys from dictionary with length more than 4
print('\nList Comprehenstion to get Keys of Certain Length from Dict \n')

nameD = {'name':'abcd','phn':'1234568790','ad':'&&&&','email':'abc@g.com'}
keyList = [key for key,value in nameD.items() if len(key)>=4]
print(keyList)

#Bonus Challenge 2 - Nested List Comprehension
print('\nNested List Comprehension to get No\'s divisible by 5 \n')

expList = [[10,20,30],[1,2,3],[-30,-20,-15]]
result = [val for sublist in expList for val in sublist if val%5==0]
print(result)

"""From the expList of Lists containing numbers
and the new list is created of numbers divisible by 5"""












