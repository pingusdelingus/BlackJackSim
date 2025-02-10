import sys

sys.setrecursionlimit(1500)


int_to_factorial = {}

def factorial(n:int) -> int:
    if n == 1 or n == 0:
        return 1
    if n in int_to_factorial:
        return int_to_factorial[n]
    else:
        return n * factorial(n - 1 )


x = input("what int you want")
x = int(x)

print(factorial(x))
