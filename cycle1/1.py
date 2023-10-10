print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print("Non-prime numbers in the interval are:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num)
                break
