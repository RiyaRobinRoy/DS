print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
n = int(input("Enter any number:"))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("This is a perfect number")
else:
    print("This is not a perfect number")
