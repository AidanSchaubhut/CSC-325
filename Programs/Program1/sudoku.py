import sys
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

  
  # go through all the elements of the group which are alredy sorted from
  # smallest to largest cardinality
  for i in range(len(group)):
  # get the cardinality of the set       
    cardinality = len(group[i])
  # if there are cardinality sets with cardinality elements then the other
  # sets can't have any of these values in them since these sets will have
  # to each have one of the cardinality values 

    # This condition was generated with Open AI's GPT-4 model.
    # Prompt: "Write a condition that checks if the number of sets with a given cardinality is equal to the cardinality."
    if sum(1 for s in group if len(s) == cardinality) == cardinality:
  # go through the sets and for each set different from the given set take
  # out all the elements that are in given set
      for j in range(len(group)):
        if i != j and not(set_equals(group[i], group[j])):
          original_len = len(group[j])
          group[j].difference_update(group[i])
          if len(group[j]) != original_len:
            changed = True
  
  return changed
  
def rule2(group):

  # This function was generated using Open AI's GPT-4 model.
  # Promt: "Write a function that creates a union of all sets in a group except for the set at the given index."
  def union_of_others(index):
    # Get all other sets
    other_sets = group[:index] + group[index+1:]
    # Perfrom the union operation
    union_set = HashSet()
    for s in other_sets:
      union_set.update(s)
    return union_set
  ### IMPLEMENT THIS FUNCTION ###

  changed = False
  # RULE 2 - Reduce set size by throwing away elements that appear in other
  # sets in the group
  for i in range(len(group)):
    # Get the current set
    cur_set = group[i]

    # Get the union of all other sets
    union_set = union_of_others(i)

    unique_elements = cur_set.difference(union_set)

    if unique_elements:
      cur_set.clear()
      for element in unique_elements:
        cur_set.add(element)
      changed = True

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
  file = open(sys.argv[1], "r")
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
  

  reduce(matrix)  

  print()
  print("Solution:")
  printMatrix(matrix)
  
main()
