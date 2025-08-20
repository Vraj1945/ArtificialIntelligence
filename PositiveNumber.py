#Program to print all positive numbers in a range.
List1 = [12, -7, 5, 64, -14]
print("Input: list1 =", List1)
print("Output:", end=" ")
for n in List1:
    if n > 0:
        print(n, end=", ")

List2 = [12, 14, -95, 3]
print("\nInput: list2 =", List2)
Positive=[]
for n in List2:
    if n > 0:
        Positive.append(n)
print("Output:", Positive)
