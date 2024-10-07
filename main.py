isPossible = False
result = 0
file = open("стандартный ввод.txt", "r")
data = []
with file:
    for line in file:
        data.append([float(x) for x in line.split()])

print(data)

def calculate_cost(x, check):
    wlh = x[0]
    w = wlh[0]
    l = wlh[1]
    h = wlh[2]
    
    s1 = w*h
    s2 = l*h
    
    door_s = x[2][0] * x[2][1]
    
    if(2*s1 <= x[1][0]) and ((2*s2 - door_s) <= x[1][2]):
        check = True
        result = (x[1][0] * x[1][1]) + (x[1][2] * x[1][3])
    
    if (check):
        f = open("стандартный вывод.txt", "w")
        f.write(str(result))
        f.close()
    else:
        f = open("стандартный вывод.txt", "w")
        f.write("-1")
        f.close()
        
calculate_cost(data, isPossible)
file.close()