# Нужно выяснить, сколько нулей имеет данное число в конце.

def end_zeros(num:int):
    zeros = 0 
    num = str(num)
    if num[-1] != '0': return 0
    for i in range(len(num)-1, -1, -1):
        if num[i] == '0':
            zeros += 1 
        else: return zeros
    return zeros
    
print(end_zeros(str(101)))