import sys, copy
from hashSet import HashSet

def getColumn(matrix, colIndex):
  col = []
  for rowIndex in range(9):
    col.append(matrix[rowIndex][colIndex])
    
  return col

def getSquare(matrix, rowIndex, colIndex):
  square = []
  for i in range(rowIndex, rowIndex+3): 
    for j in range(colIndex,colIndex+3):
        square.append(matrix[i][j])
        
  return square

def getGroups(matrix):
  groups = []
  # get rows
  for i in range(9):
    groups.append(list(matrix[i]))
  # get columns
  for i in range(9):
    groups.append(getColumn(matrix,i))
  # get squares
  # squares are processed left-right, up-down
  for i in range(0,9,3): 
    for j in range(0,9,3):
      groups.append(getSquare(matrix,i,j))     

  return groups

def cardinality(x):
  return len(x)

def set_equals(set1, set2):
  if cardinality(set1) != cardinality(set2):
    return False
  for item in set1:
    if item not in set2:
      return False
  return True

# Help implement the rules


def rule1(group):
  changed = False
  # RULE 1 - You have to look for duplicate sets (i.e. set([1,6])). If you 
  # have same number of duplicate sets in a group (row, column, square) as 
  # the cardinality of the duplicate set size, then they must each get one 
  # value from the duplicate set. In this case the values of the duplicate 
  # set may be removed from all the other sets in the group. 
  # go through all the elements of the group which are already sorted from
  # smallest to largest cardinality
  for i in range(len(group)):
    # get the cardinality of the set
    cardinality = len(group[i])
    
    # if there are cardinality sets with cardinality elements then the other
    # sets can't have any of these values in them since these sets will have
    # to each have one of the cardinality values 
    if sum(1 for s in group if len(s) == cardinality) == cardinality:
      # go through the sets and for each set different from the given set take
      # out all the elements that are in the given set
      for j in range(len(group)):
        if len(group[j]) != cardinality:
          group[j].difference_update(group[i])
          if len(group[j]) == 0:
            return True
  
  return changed
  
def rule2(group):
  ### IMPLEMENT THIS FUNCTION ###

  changed = False
  # RULE 2 - Reduce set size by throwing away elements that appear in other
  # sets in the group
  # Iterate over each set in the group
  # Create a dictionary to store items to be removed from each set

  # pick an element of the group

  # for all the other elements of the group remove the elements that appear
  # in other elements of the group. These can be satisfied by other elements
  # of the group

  # When done, if there is one value left then it can only be satisfied by
  # this cell. This is a most constrained rule. If end up with 0 elements,
  # then not enough information yet to constrain this choice. If didn't
  # improve the situation at all, let's continue looking at other elements
  # in the row. 

  return changed

def reduceGroup(group):
  changed = False 
  # this sorts the sets from smallest to largest based cardinality
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

def solutionViable(matrix):
  for i in range(9):
    for j in range(9):
      if (len(matrix[i][j])) == 0:
        return False
      
  return True

def union(group):
  result = set([])
  for s in group:
    result.update(s)
  return result

def soulutionOK(matrix):
  # Check for cells
  for i in range(9):
    for j in range(9):
      if (len(matrix[i][j])) != 1:
        return False
      
  # Check for rows
  for theRow in matrix:
    if len(union(theRow)) != 9:
      return False
    
  # Check for cols
  for j in range(9):
    theCol = getColumn(matrix, j)
    if len(union(theCol)) != 9:
      return False
    
  # Check for squares
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      theSquare = getSquare(matrix, i, j)
      if len(union(theSquare)) != 9:
        return False
      
  # Everything checks out
  return True

def solve(matrix):
  reduce(matrix)

  if not solutionViable(matrix):
    return None
  
  if solutionOK(matrix):
    return matrix
  
  print("Searching...")

  for i in range(9):
    for j in range(9):
      if len(matrix[i][j]) > 1: # Used to see if there is more than 1 element in the cell
        for k in matrix[i][j]:
          mcopy = copy.deepcopy(matrix)
          mcopy[i][j] = set([k])

          result = solve(mcopy)

          if result != None:
            return result
          
  return None


def printMatrix(matrix):
  for i in range(9):
    for j in range(9):
      if len(matrix[i][j]) != 1:
        sys.stdout.write("x ")
      else:
        for k in matrix[i][j]:
          sys.stdout.write(str(k) + " ")

    sys.stdout.write("\n")

def main():
  #file = open(sys.argv[1], "r")
  file = open("test-1.txt", "r")
  matrix = []

  for line in file:
    lst = line.split()
    row = []

    for val in lst:
      if val == 'x':
        s = HashSet(range(1,10))
      else:
        s = HashSet([eval(val)])
      row.append(s)

    matrix.append(row)

  print("Solving this puzzle:")
  printMatrix(matrix)

  print("Begin solving...")

  matrix = solve(matrix)

  if matrix == None:
    print("No solution found")
    return

  print()
  print("Solution:")
  printMatrix(matrix)
  
main()
