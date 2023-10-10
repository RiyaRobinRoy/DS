import numpy as np
print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
even_numbers = np.arange(2, 31, 2)
elements_step_2 = even_numbers[2:9:2]
print("a. Elements from index 2 to 8 with step 2:")
print(elements_step_2)
last_3_elements = even_numbers[-3:]
print("b. Last 3 elements of the array using negative index:")
print(last_3_elements)
alternate_elements = even_numbers[::2]
print("c. Alternate elements of the array:")
print(alternate_elements)
last_3_alternate_elements = alternate_elements[-3:]
print("d. Last 3 alternate elements:")
print(last_3_alternate_elements)

