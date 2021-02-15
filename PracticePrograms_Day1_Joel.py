#Question 1

name = ["john","jake","jack","george","jenny","jason"]
names = set(name)
for n in names:
    if len(n) < 5 and 'e' not in n:
        print(n)

#Question 2

sampleString = "python"
print("c"+sampleString[1:])

#Question 3

d = {"name":"python","ext":"py","creator":"guido"}
print(d.keys())
print(d.values())

#Question 4

fizzBuzz = input("Enter the number to execute FizzBuzz:")
for i in range(1,int(fizzBuzz)+1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")   
    else:
        print(str(i))

#Question 5

guessNum = input("Enter your Guess Number")
hCNum = 10

if int(guessNum) > hCNum:
    print("Your Guess was Higher")
elif int(guessNum) < hCNum:
    print("Your Guess was Lower")
else:
    print("Your Guess was Exact")
