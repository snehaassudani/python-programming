# Experiment 1:
AIM:
To write and execute a python program to demonstrate various data types and operators in python
Algorithm
1. Start the program
2. Declare variables using different data types such as:
   Integer
   Float
   String
   Boolean
   List
   Tuple
   Dictionary
   Set
3. Display
4.
a = 10
b = 3.5
name = "Alice"
is_student = True
numbers = [10, 20, 30]
colors = ("Red", "Green", "Blue")
student = {
    "Name": "Alice",
    "Age": 20
}
fruits = {"Apple", "Banana", "Mango"}

print("Data Types:")
print("Integer:", a)
print("Float:", b)
print("String:", name)
print("Boolean:", is_student)
print("List:", numbers)
print("Tuple:", colors)
print("Dictionary:", student)
print("Set:", fruits)

x = 15
y = 4

print("\nArithmetic Operators:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponent:", x ** y)

print("\nComparison Operators:")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

print("\nLogical Operators:")
print("x > 10 and y < 5:", x > 10 and y < 5)
print("x > 20 or y < 5:", x > 20 or y < 5)
print("not(x > 10):", not (x > 10))

print("\nAssignment Operators:")
z = 5
print("Initial z:", z)
z += 3
print("z += 3:", z)
z *= 2
print("z *= 2:", z)

print("\nMembership Operators:")
print("20 in numbers:", 20 in numbers)
print("50 not in numbers:", 50 not in numbers)

print("\nIdentity Operators:")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 == list3:", list1 == list3)
