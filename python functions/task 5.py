'''Task 5: Write a function calculator(a, b, operation) 
which takes two numbers and 
an operation (add, subtract, multiply, divide).
✅ Test Case:

print(calculator(10, 5, "add"))       # 15
print(calculator(10, 5, "subtract"))  # 5
print(calculator(10, 5, "multiply"))  # 50
print(calculator(10, 5, "divide"))    # 2.0'''

def calculator(a, b, operation):
    if operation=="add":
        return a+b
    if operation=="subtract":
        return a-b
    if operation=="multiply":
        return a*b
    if operation=="divide":
        return a/b
print(calculator(10,5,"add"))
print(calculator(10,5,"subtract"))
print(calculator(10,5,"multiply"))
print(calculator(10,5,"divide"))