def genList(arr):
    list1 = []
    for i in arr:
        sumGlass = 0
        for j in i:
            if j in 'аеёиоуыэюя':
                sumGlass += 1
        list1.append(sumGlass)
    return list1

def rhythm(poem, fun):
    poem = poem.split()
    list1 = fun(poem)
    return len(list1) == list1.count(list1[0])

text = input('Введите стих: ')
if rhythm(text,genList):
    print('Парам пам-пам')
else:
    print('Пам парам')