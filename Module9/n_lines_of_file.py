print("Ankur Kumar Kushwaha   1900300100034")

f = open("test1.txt", "w")
f.write("I am ankur\n")
f.write("This is my first file in python\n")
f.close()

f = open("test1.txt", "r")
print(f.read())
f.close()