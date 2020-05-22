"""
A back tracking approach for finding the best colored  grid. 
G:Green
B:Blue
R:Red
W:White
Y:Yellow
Grid is a squared matrix
Matrix is initialized with 0 values. A matrix with all non zero elements is a possible solution

Possible solution space
A color in the matrix can not have beeds same color in adjacent

This 

B B G G
B B G G 

is a invalid configuration

while

B G B G
G B G B 
is a valid configuration with possible solutions
Array start from 1 index 0th index is kept for background
"""
import numpy as np # for efficient matrix manipulation
import sys #import to increase the number of possible recursion. In python the recursion limit is 99 this increases the bar of the same


def isColor(arr):
    """
    Checks if all the elements of the array are colored
    params:
    arr: Input array
    return
    True: if all elements are colored
    False: if all elements are not colored
    """
    if len(np.flatnonzero(arr==0))==0:
        return True
    else:
        return False

def getnextIndex(arr):
    """
    Generates the next non colored index
    params:
    arr: Input array
    returns
    index(row,column) of the next non colored index
    """
    if not isColor(arr):
        index = list(np.flatnonzero(arr==0))[0] # generates the first non zero index
        return (index//dim,index%dim) #returns the result

def decrementColor(color_index):
    """
    Decrements the available beeds
    params:
        color_index: Index of the colored beed for global dictionary mentioned
    """
    global colors
    colors[color_index]-=1

def incrementColor(color_index):
    """
    Increments the available beeds (used in Backtracking )
    params:
        color_index: Index of the colored beed for global dictionary
    """
    global colors
    colors[color_index]+=1

def getMaxColor(color_list=None):
    """
    Gives the index of maximum colored beed
    params:
        color_list: list of  Possible beed colors in the current space of the problem
    returns:
        indices: indices of possible colored beeds  having maximum count 
    """
    if color_list is None: # if color_list is None then the entire color dictionary is considered
        m =max(colors)
        if m!=0:
            #indices of all beeds having max count
            indices = sorted(list(np.flatnonzero(colors==m)),reverse=True)
        else:
            indices=[]
    else:        
        l = [colors[i] for i in color_list]
        m = max(l)
        if m!=0:
            #indices of all beeds having max count
            indices = sorted(list(np.flatnonzero(colors==m)),reverse=True)
            indices = [i for i in indices if i in color_list]
        else:
            indices=[]    
    return indices    

def isValid(pos):
    """
    gets the valid positioning with respect to grid configuration
    params:
        pos: row_index column_index
    returns:
        True if the value is correct
        False otherwise
    """
    return (pos[0]>=0 and pos[0]<dim and pos[1]>=0 and pos[1]<dim)

def getValidColor(pos):
    """
    generates valid list of colors
    Since the matrix is parsed left to right top to bottom constraint checks of (x-1,y) and (x,y-1)        
    params
        pos: row_index,column_index
    returns: 
        color_list: list of all possible colors following the 4 connected constrained
    """
    color_list=[]
    if isValid((pos[0]-1,pos[1])):
        color_list.append(grid[pos[0]-1,pos[1]])
    if isValid((pos[0],pos[1]-1)):
        color_list.append(grid[pos[0],pos[1]-1])
    color_list =[i for i in range(1,len(colors)) if i not in color_list]
    return color_list

def colorGrid(arr):
    """
    Solves the color grid problem
    params:
        arr: input array
    returns:
        True: If solution is found
        False: Other wise    
    """
    #If solution is achieved
    if isColor(arr):
        return True
    else:
        #Get the next non colored index
        x,y = getnextIndex(arr)
        #Get the possible color to be assigned 
        color_list=getMaxColor(getValidColor((x,y)))
        #print(x,y,color_list,colors)
        #If no possible colors are to be assigned then there are no possible result space which satisfies the constraint
        if len(color_list)==0:
            return False
        else:
            for i in color_list:

                arr[x,y] = i
                decrementColor(i)
                #If the current assignment results in to a solution return solution
                if  colorGrid(arr):
                    return True    
                #BackTrack    
                incrementColor(i)
                arr[x,y] = 0
            return False          


#Inputs
#12 red beads (R) and 13 blue beads (B)
dim = 5
grid = np.zeros((dim,dim),dtype='uint8')
color_map = {1:'R',2:'B'}
colors=np.array([0,12,13],dtype='uint8')
colorGrid(grid)
#write results
w = open("output_question_5_1",'w')
for i in range(dim):
    for j in range(dim):
        w.write(str(color_map[grid[i,j]])+" ")
    w.write("\n")
w.close()
#5_2        
#print(grid)
dim = 64 
sys.setrecursionlimit(dim**3)
grid = np.zeros((dim,dim),dtype='uint8')
color_map = {1:'R',2:'B',3:'G',4:'W',5:'Y'}
colors=np.array([0,139,1451,977,1072,457],dtype='uint32')

#Write results
colorGrid(grid)
w = open("output_question_5_2",'w')
for i in range(dim):
    for j in range(dim):
        w.write(str(color_map[grid[i,j]])+" ")
    w.write("\n")
w.close()    