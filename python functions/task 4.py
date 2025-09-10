'''Task 4: Write a function factorial(n) 
that returns factorial of a number.
✅ Test Case:

print(factorial(5))  # 120
print(factorial(0))  # 1'''

def factorial(n):
    fact =1
    for i in range (1,n+1):
        fact*=i
    return fact
print(factorial(5))
print(factorial(0)) 
