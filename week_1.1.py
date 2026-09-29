# Basic Python examples ready to paste and run

print("Hello, Python!")

x = 10
y = 3.5
name = "Alice"
print(x, y, name)

integer_value = 5
float_value = 2.5
string_value = "hello"
boolean_value = True
print(type(integer_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))

a = 7
b = 2
print(a + b)   # 9
print(a - b)   # 5
print(a * b)   # 14
print(a / b)   # 3.5
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 49

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1:3])
fruits.append("date")
print(fruits)

person = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}
print(person["name"])
print(person.get("age"))

age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

for i in range(3):
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

text = "Python"
print(text[0])
print(text[:2])
print(text[:4])
print(text[:])


txt1="My name is {fname},I'm {age}".format(fname = "John", age = 36)
txt2="My name is {0},I'm {1}".format("John",36)
txt3="My name is {},I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

n = int(input("Enter a number: "))
even_odd(n)

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Array:", a)
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

import numpy as np

a = np.zeros([3, 3])
b = np.ones([2, 4])
print(a)
print(b)
