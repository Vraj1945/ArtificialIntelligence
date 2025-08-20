# Fibonacci Series
a, b = 0, 1
Limit = int(input("Enter the last digit for the fibonnaci series: "))
print("Fibonacci Series up to", Limit, ":")
while a<=Limit:
    print(a, end=" ")
    a, b = b, a + b
