#MY DAILY DAIRY

print("Hello L&T Technology Services")
print("hello world")
print("Second Commit")

def mr:
num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


num = 8 


num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))



a = 5
b = 6
c = 7
# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

x = 5
y = 10
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)


# Program to generate a random number between 0 and 9

# importing the random module
import random
print(random.randint(0,9))
