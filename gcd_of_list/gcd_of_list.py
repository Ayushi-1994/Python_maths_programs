def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_list(nums):
    result = nums[0]
    for n in nums[1:]:
        result = gcd(result, n)
    return result

print(gcd_list([12, 18, 24]))
