print("Ankur Kumar Kushwaha   1900300100034")

list1 = {"Hi", "Hello"}
f = open("test1.txt", "w")
for element in list1:
    f.write(element + "\n")
f.close()

f = open("test1.txt", "r")
print(f.read())
f.close()