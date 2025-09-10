'''Task 7: Write a function multiply_all(*args) 
that multiplies all numbers passed.
✅ Test Case:

print(multiply_all(2, 3, 4))   # 24
print(multiply_all(1, 5, 7, 2)) # 70'''

def multiply_all(*args):
    result =1
    for i in args:
        result*=i
    return result
print(multiply_all(2, 3, 4))