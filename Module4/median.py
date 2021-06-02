print("Ankur Kumar Kushwaha  1900300100034")

a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median of the three numbers is ", median)