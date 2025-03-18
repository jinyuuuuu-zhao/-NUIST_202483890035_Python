# Add Two Numbers in Python
# Author: Your Name here
# Using the + Operator
a = 15
b = 12
# Adding two numbers
res = a + b
print(res)


# Add Two Numbers in Python
# Author: ZhaoYujin
# Using user input
# taking user input
a = input("First number: ")
b = input("Second number: ")
# converting input to float and adding
res = float(a) + float(b)
print(res)

# Add Two Numbers in Python
# Author: Your Name here
# Using a function
# function to add two numbers
def add(a,b):
 #converting input to float and adding
 result = float(a) + float(b)
 return result
# taking user input
a = input("First Number: ")
b = input("Second Number: ")
# calling function
res = add(a,b)
print("The Answer is:")
print(res)

def factorial_while(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1  
    return result
number = int(input("Please enter a number:"))
print(factorial_while(number))

def factorial_for(num):
    result = 1
    for i in range(1,num + 1):
        result = result * i
    return result

number = int(input("Please enter a number:"))
print(factorial_for(number))

studentNames = ["Lisa","Liam","Leo","Linda"]
for name in studentNames:
    print(name + "Evans")

new_name = input("Please add a name:")
studentNames.append(new_name)

for name in studentNames:
    print(name + "Evans")

