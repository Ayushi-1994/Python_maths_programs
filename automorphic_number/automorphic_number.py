def is_automorphic(n):
    return str(n*n).endswith(str(n))

print(is_automorphic(25))
