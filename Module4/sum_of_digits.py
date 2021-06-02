print("Ankur Kumar Kushwaha  1900300100034")

num=int(input("Enter a number:"))
result = 0
while(num>0):
    rem = num % 10
    result = result + rem
    num = int(num / 10)
print("The sum of the digits :",result)