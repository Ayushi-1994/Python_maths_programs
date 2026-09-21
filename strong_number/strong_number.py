def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

def is_strong(n):
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == n

print(is_strong(145))
