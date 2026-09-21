def is_palindrome(n):
    original = n
    reversed_num = 0

    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n //= 10

    return original == reversed_num

print(is_palindrome(121))
