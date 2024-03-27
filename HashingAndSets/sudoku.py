import sys
from HashSet import HashSet

def getGroups(matrix):
    # groups for rows
    # groups for cols
    # groups for squares
    pass
    

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

main()