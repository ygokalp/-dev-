# Function to calculate the sum of even Fibonacci terms below a limit
def fibonacci_sum(limit):
    a, b = 1, 2
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        # Update values for the next Fibonacci numbers
        temp = a
        a = b
        b = temp + b

    return even_sum

# Set the limit
limit = 4000000

# Call the function and print the result
result = fibonacci_sum(limit)
print("Sum of even-valued Fibonacci terms below", limit, "is:", result)
