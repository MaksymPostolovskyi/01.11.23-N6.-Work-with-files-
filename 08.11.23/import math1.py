import math

def data(file_path='input.txt'):
    with open(file_path, 'r') as file:
        b1 = float(file.read())
        a1 = math.atan(b1)
        y = a1/(b1**2 + math.sqrt(a1))
       

    return b1, a1, y

result = data()  

result_str = f"b1: {result[0]}\n a1: {result[1]}\n y: {result[2]}"

print(result_str)


with open("output.txt", 'w') as f:
    f.write(result_str)
