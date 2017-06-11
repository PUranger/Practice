def summation(a, b):
    while b:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a


print summation(5,11)
