print("RIYA ROY - SJC22MCA-2045")
print("BATCH: 2022-2024")
s1 = int(input("Enter 1st side:"))
s2 = int(input("Enter 2nd side:"))
s3 = int(input("Enter 3rd side:"))
if s1 == s3 == s2:
    print("The given triangle is equilateral")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("The given triangle is isoceles")
else:
    print("The given triangle is scalene")
