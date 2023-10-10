print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
N = int(input("Enter the limit:"))
num1 = 0
num2 = 1
for i in range (N):
    print(num1,end=" ")
    num3=num1+num2
    num1=num2
    num2=num3
