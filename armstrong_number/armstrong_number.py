def is_armstrong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10

    return total == original

print(is_armstrong(153))
