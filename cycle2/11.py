import numpy as np

print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
rows, cols = 3, 3
X = np.random.randint(1, 10, size=(rows, cols))
cube_multiply = np.multiply(X, np.multiply(X, X))
cube_power = np.power(X, 3)
cube_double_star = X ** 3
print("Cube using multiply():")
print(cube_multiply)
print("\nCube using power():")
print(cube_power)
print("\nCube using ** operator:")
print(cube_double_star)
identity_matrix = np.identity(rows)
print("\nIdentity Matrix:")
print(identity_matrix)
powers = [2, 3, 4]
powered_matrix = np.power(X, powers)
print("\nMatrix raised to different powers:")
print(powered_matrix)
