# Нужно удалить все элементы до данного.

def remove_all_before(items, value):
    for item in items:
        if item < value:
            del(item)
        else: print(item)
            
print(remove_all_before(items = [1, 2, 3, 4, 5], value = 3))
print(remove_all_before(items = [1, 1, 2, 2, 3, 3], value = 2))

