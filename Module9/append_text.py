print("Ankur Kumar Kushwaha   1900300100034")

f = open("test1.txt", "a")
f.write("Appending in Python\n")
f.close()

f = open("test1.txt", "r")
print(f.read())
f.close()