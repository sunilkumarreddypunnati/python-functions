'''Task 6: Write a function outer() which prints "Outer function" 
and defines an inner() function that prints "Inner function".
✅ Test Case:

outer()
# Output:
# Outer function
# Inner function'''

def  outer():
    print("Outer function")
    def inner():
        print("inner function")
    inner()
outer()