
# Factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

# Fibonacci Sequence
def get_fib(position):
    if position <= 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)

# Test cases
x = int(input("What's the number?"))
print(factorial(x))

x = int(input("What's the number?"))
print(get_fib(x))