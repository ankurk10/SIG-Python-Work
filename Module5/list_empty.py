print("Ankur Kumar Kushwaha   1900300100034")

list = []
n = int(input("Enter number of elements in the list : "))
print("Enter the elements of the list")
for i in range(0, n):
    ele = int(input())
    list.append(ele)

print(list)
if len(list) == 0 :
    print("List is empty")
else :
    print("List is not empty")
