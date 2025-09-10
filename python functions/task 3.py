'''Task 3: Write a function even_or_odd(n) 
that returns "Even" if number is even, else "Odd".
✅ Test Case:

print(even_or_odd(10))  # Even
print(even_or_odd(7))   # Odd'''

def even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(10))
print(even_or_odd(7))