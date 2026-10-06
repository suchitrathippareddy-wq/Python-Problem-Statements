def gcd_lcm(a, b):

    gcd = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    lcm = (a * b) // gcd

    return gcd, lcm


a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

gcd, lcm = gcd_lcm(a, b)

print("GCD =", gcd)
print("LCM =", lcm)