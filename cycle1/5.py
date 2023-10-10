print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
import math

a = int(input("Enter coefficient of x^2:"))
b = int(input("Enter coefficient of x:"))
c = int(input("Enter constant:"))
d = b * b - (4 * a * c)
if d >= 0:
    x1 = float(-b + math.sqrt(d)) / (2 * a)
    x2 = float(-b - math.sqrt(d)) / (2 * a)
    print(f"Root1:{x1:.2f}")
    print(f"Root2:{x2:.2f}")
else:
    print("invalid roots")
