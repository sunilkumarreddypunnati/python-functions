'''Task 10: Squares using Map

Problem: Return the squares of numbers using map() and lambda.
Input: List of integers.
Output: List of squares.
Sample Input:

1 2 3 4 5

Sample Output:

[1, 4, 9, 16, 25]'''

numbers =[1, 2, 3, 4, 5]
squares=list(map(lambda x:x**2,numbers))
print(squares)