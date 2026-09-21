def is_harshad(n):
    temp = n
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    return n % digit_sum == 0

print(is_harshad(18))
