## Example 1: Using recursion
def fib(n):
 if n==1 or n==2:
  return 1
 return fib(n-1)+fib(n-2)
print fib(7)

##Using looping technique
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print fib(7)
