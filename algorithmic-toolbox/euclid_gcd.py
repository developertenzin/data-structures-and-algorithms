def euclid_gcd(a, b):
    if b == 0:
        return a
    return euclid_gcd(b, a%b)

print(euclid_gcd(24, 54))
