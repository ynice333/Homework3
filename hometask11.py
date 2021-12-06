# Нужно найти подстроку, заключенную между двумя мaркерами.

def between_markers(text):
    list1 = text = 'What is >apple<'
    list2 = []
    for i in list1:
        a = i.split(">")
        for b in a:
            a = b.split("<")
            list2.append(a)
            print(list2)

print(between_markers(text = 'What is >apple<'))