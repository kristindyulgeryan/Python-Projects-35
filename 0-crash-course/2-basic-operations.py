import math


# basic oparations
x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)

# string concatination
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

print("My name is " + first_name + " and my last name is " + last_name)
# f strings
print(f"hello my name is {first_name} and my last name is {last_name}")


# int floor division

a = 17
b = 5

print(a/b)  # result 3 (rounds down ) or it is 3.4
print(a//b)  # result 3 (rounds down ) or it is 3.4


# assign multiple values
i, j, k = 1, 2, 3
print(i, j, k)

# swap values
m = 20
n = 10
m, n = n, m
print(m, n)

# comparison operators
c = 5
d = 10
print(c == d)
print(c != d)
print(c < d)
print(c > d)
print(c >= d)
print(c <= d)


# logical operators
a = True
b = False

print(a and b)
print(a or b)
print(not b)


# string slicing
text = "Python programming"
print(text[0:6])
print(text[7:])
# reverse
print(text[::-1])


# string formatting with .format()
name = "Alice"
age = 25
msg = "My name is {} and I am {} years old".format(name, age)
print(msg)


# using placeholders
msg2 = "My name is {0} and I am {1} years. {0} is nice name".format(name, age)
print(msg2)


# math module operations
print(math.pi)
print(math.sqrt(16))
print(math.floor(4.7))  # 4.0
print(math.ceil(5.3))  # 6.0
print(math.pow(2, 3))  # 8


pi = 3.141592653589793
print(round(pi, 2))
