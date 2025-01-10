import math
valueOfA = int(input("input for A : "))
valueOfB = int(input("input for B : "))
valueOfC = int(input("input for C : "))
discriminant = ((valueOfB**2) - ((4 * valueOfA) * (valueOfC))) / (2 * valueOfA)
if discriminant >= 0:
    print(-valueOfB + math.sqrt(discriminant))
else:
    print("undefined")
    discriminant = ((valueOfB**2) - ((4 * valueOfA) * (valueOfC))) / (2 * valueOfA)
if discriminant >= 0:
    print(-valueOfB - math.sqrt(discriminant))
else:
    print("unedfined")
    discriminant = (valueOfB**2) - (4 * valueOfA * valueOfC)
if discriminant >= 0:
    root1 = (-valueOfB + math.sqrt(discriminant)) / (2 * valueOfA)
    root2 = (-valueOfB - math.sqrt(discriminant)) / (2 * valueOfA)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
else:
    print("unedfined")
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("undefined")
    import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c  # Calculate the discriminant
    if discriminant < 0:
        print("undefined")  # No real roots
        return None
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)  # First root
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)  # Second root
    return root1, root2

# Input values for a, b, and c
valueOfA = int(input("Input for A: "))
valueOfB = int(input("Input for B: "))
valueOfC = int(input("Input for C: "))

# Solve the quadratic equation
roots = solve_quadratic(valueOfA, valueOfB, valueOfC)

# If roots exist, print them
if roots:
    root1, root2 = roots
    print(f"The roots are: {root1} and {root2}")

