import numpy as np
print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
array_2d = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]])
print("a. All elements excluding the first row:")
print(array_2d[1:])
print("b. All elements excluding the last column:")
print(array_2d[:, :-1])
print("c. Elements of 1st and 2nd column in 2nd and 3rd row:")
print(array_2d[1:3, :2])
print("d. Elements of 2nd and 3rd column:")
print(array_2d[:, 1:3])
print("e. 2nd and 3rd element of 1st row:")
print(array_2d[0, 1:3])
print("f. Elements from indices 4 to 10 in descending order:")
print(array_2d.flatten()[4:11][::-1])