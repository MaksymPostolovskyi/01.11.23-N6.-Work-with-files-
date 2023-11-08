import math

file = open("input.txt", "r")
b1 = float(file.read())
a1 = math.atan(b1)
y = a1/(b1**2 + math.sqrt(a1))
print(f"b1 = {b1}\na1 = {a1}\ny = {y}")
    
f = open("output.txt", "w")
f.write(f"a1 = {a1}\ny = {y}")