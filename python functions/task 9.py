'''Task 9: Maximum of Two Numbers

Problem: Find the maximum of two numbers using a lambda function.
Input: Two integers.
Output: Maximum number.
Sample Input:
10 20

Sample Output:
20'''

Maximum=lambda a,b:a if a>b else b
print(Maximum(10,20))