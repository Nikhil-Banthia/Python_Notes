def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example: Generate the first 10 numbers in the Fibonacci series
n = 10
fib_series = [fibonacci_recursive(i) for i in range(n)]
print(f"Fibonacci series up to {n} numbers: {fib_series}")
