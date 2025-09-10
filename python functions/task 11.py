'''Task 11: Filter Divisible by 10

Problem: Extract numbers divisible by 10 using filter().
Input: List of integers.
Output: List of numbers divisible by 10.
Sample Input:

10 15 20 25 30

Sample Output:

[10, 20, 30]'''

numbers=[10,15,20,25,30]
divisible=list(filter(lambda x: x%10==0,numbers))
print(divisible)