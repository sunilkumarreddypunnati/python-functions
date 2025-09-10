'''Task 13: Generator for Even Numbers

Problem: Yield even numbers up to n using a generator.
Input: Integer n.
Output: Even numbers from 0 to n.
Sample Input:
10

Sample Output:
0 2 4 6 8 10'''

def gen_fun(n):
    for i in range(0,n+1):
        if i%2==0:
          yield i
for i in gen_fun(10):
        print(i,end=' ')