isPossible = False
file = open("стандартный ввод.txt", "r")
data = []
with file:
    for line in file:
        data.append([float(x) for x in line.split()])

print(data)

def calculate_cost(x):
    if (isPossible):
        f = open("стандартный вывод.txt", "w")
        f.write("yes")
        f.close()
    else:
        f = open("стандартный вывод.txt", "w")
        f.write(-1)
        f.close()
        
# calculate_cost(c)
file.close()