'''Task 12: Reduce for Sum

Problem: Find the sum of numbers using reduce().
Input: List of integers.
Output: Sum of all numbers.
Sample Input:
5 10 15 20

Sample Output:
50
'''
from functools import reduce
numbers=[5,10,15,20]
sum_of = reduce (lambda x,y:x+y,numbers)
print(sum_of)