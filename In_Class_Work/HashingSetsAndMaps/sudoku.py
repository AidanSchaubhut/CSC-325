import sys
from HashSet import HashSet

def getColumn(matrix, colIndex):
    col = []
    for rowIndex in range(9):
        col.append(matrix[rowIndex][colIndex])
    return col

def getSquare(matrix, rowIndex, colIndex):
    square = []
    for i in range(rowIndex, rowIndex + 3):
        for j in range(colIndex, colIndex + 3):
            square.append(matrix[i][j])
    return square

def getGroups(matrix):
    groups = []
    # groups for rows
    for i in range(9):
        groups.append(list(matrix[i]))
    
    # groups for cols
    for i in range(9):
        groups.append(getColumn(matrix, i))

    # groups for squares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            groups.append(getSquare(matrix, i, j))

    return groups

def cardinality(x):
    return len(x)

def reduceGroup(group):
    changed = False
    group.sort(key=cardinality)
    changed = rule2(group)
    changed = rule1(group)
    return changed

def reduceGroups(groups):
    changed = False
    for group in groups:
        if reduceGroup(group):
            changed = True
    return changed
    
def reduce(matrix):
    changed = True
    groups = getGroups(matrix)

    while changed:
        changed = reduceGroups(groups)


def printMatrix(matrix):
    for i in range(9): # Row
        for j in range(9): # Column
            if len(matrix[i][j]) != 1:
                sys.stdout.write("x ")
            else:
                for k in matrix[i][j]: 
                    sys.stdout.write(str(k) + " ")
        sys.stdout.write("\n")

def main():
    file = open("sudoku.txt", "r")
    matrix = []

    for line in file:
        lst = line.split()
        row = []
        
        for val in lst:
            if val == 'x':
                s = HashSet(range(1, 10))
            else:
                s = HashSet([int(val)])
            row.append(s)
        
        matrix.append(row)

    print("Solving this sudoku: ")

    printMatrix(matrix)

    reduce(matrix)
    print()
    print("Solution: ")
    printMatrix(matrix)

main()