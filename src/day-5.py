def greet():
    print("Hello, welcome to the Python tutorial!")

greet()

#arguement and return value
def add_numbers(a,b):
    return a+b

result=add_numbers(5,10)
print(result)
   

def add_numbers(a,b):
    return a + b
result = add_numbers(5, 3)
print("The sum of 5 and 3 is:", result)
icecream = "vanilla"
def food():
    fruit = "apple"
    vegetable = "carrot"
    print(fruit,"is good for health")
    print(icecream,"is a good flavour")

food()

print("Icecream flavour outside the function:", icecream)
print("Vegetable is also good for health:", vegetable)



import math
import random 
print(math.sqrt(16))
print(random.randiant(1,10))
