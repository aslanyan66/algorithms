# Task 1

# 1.1

# ete heraxosi hamarnery sortavorvac lini O(log n) (chnayac karanq sortavorenq heraxosi hamarnery?), hakarak depqum On

# 1.2

# ete ejery hamarakalac exan grquyki apa O(log n), hakarak depqum On

# pseudocode

# function euclideanGCD(a, b):
#     while b is not 0:
#         remainder = a % b
#         a = b
#         b = remainder
#     return a

def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 18
result = gcd_euclidean(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")