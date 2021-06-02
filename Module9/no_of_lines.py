print("Ankur Kumar Kushwaha   1900300100034")

lines = 0
with open("test1.txt", 'r') as file:
    for line in file:
        lines = lines+1
print(f"Number of lines = {lines}")