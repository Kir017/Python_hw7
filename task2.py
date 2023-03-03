def printOperationTable(operation, numRows, numColumns):
    arr = [[operation(i, j) for i in range(1, numRows + 1)] for j in range(1, numColumns + 1)]
    for i in arr:
        print(*[f'{x:>4}' for x in i])
line = int(input('Введите количество строк: '))
colums = int(input('Введите количество столбцов: '))
printOperationTable(lambda x, y: x * y, line, colums)