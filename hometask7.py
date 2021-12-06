# Найдите ближайшее значение к переданному.

def nearest_value(items, value):
    found = items[0]
    for item in items:
        if abs(item - value) < abs(found - value):
            found = item
    return found

print(nearest_value(items = [4, 7, 10, 11, 12, 17], value = 9))
print(nearest_value(items = [4, 7, 10, 11, 12, 17], value = 8))
