print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
n1 = int(input("Enter the 1st number:"))
n2 = int(input("Enter the second number:"))
gcd = 1
s = min(n1, n2)
for i in range(2, s + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        break
if gcd == 1:
    print(n1, "and", n2, "are coprime")
else:
    print(n1, "and", n2, "are not coprime")
