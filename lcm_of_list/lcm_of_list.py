def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_list(nums):
    result = nums[0]
    for n in nums[1:]:
        result = lcm(result, n)
    return result

print(lcm_list([4, 6, 8]))
