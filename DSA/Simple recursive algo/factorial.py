n = int(input("Enter a number: "))

def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Iterative factorial of {n} is: {iterative_factorial(n)}")

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print(f"Recursive factorial of {n} is: {recursive_factorial(n)}")