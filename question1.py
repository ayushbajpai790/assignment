//Create a python function that can return nth fibonacci  number
def fib(n):
   if n <= 2:
      return n - 1
   else:
      return fib(n - 1) + fib(n - 2)

n=int(input("enter a number: "))
print(fib(n))
