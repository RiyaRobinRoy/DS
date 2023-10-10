import numpy as np
print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
two_dim_array = np.array([[1.1 + 2j, 3.2 + 4j, 5.1 + 6], [7.6 + 8j, 9.2 + 10j, 11.1 + 12j]], dtype=complex)
print("2D Array:")
print(two_dim_array)
num_row, num_cols = two_dim_array.shape
print(f"\na.Number of rows:{num_row}")
print(f"b.Number of colums:{num_cols}")
dimensions = two_dim_array.ndim
print(f"c.Dimention of the array:{dimensions}")
reshaped_array = two_dim_array.reshape(3, 2)
print("\nReshaped Array (3x2):")
print(reshaped_array)
