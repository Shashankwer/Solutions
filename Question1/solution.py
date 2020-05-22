"""
Given an mxn Matrix starting from the top left corner to the bottom right corner with only two possible operations allowed we need to find the possible path within which it can be reached. 

The algorithm used below is similar to A Star search space. 
1. In typical scenario the alogorithm would require finding 
possible path from all n nodes giving a problem space of O(2^n). 
Finding solution in such scenario is  computationally expensive. 

A start makes use of a heuristic approach for finding the optimal path from source to destination
The cost required to reach any path is given by f(n)=g(n)+h(n)

h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal. A* can terminate the execution when the path it chooses reaches the gola or there are no possible path from the current node. 
This reduces the complexity to polynomial scope rather than eponential time

In this apprach we extend the informed based seach of A* Algorithm with 2 heuristic involved
e.g Consider the below matrix

1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

Starting from the top left node to the bottom right node 
The min path can be achieved using RRRDDD cost 13
Similarly the max path is achived using DDDRRR cost 22

Thus starting from Top left the any path should be between 
the max heuristic and min hueristic. The path with sum of more than 22 is not achievable. Similarly the path of cost less than 13 is not achievable starting from Top left corner

These hueristic give an upper and lower bound for the search space
Based on cost heuristic the upper and lower bound of the matrix can thus be represented as

22,13   18,12   14,11   10,10  
21,15   17,13   13,11   9,9
19,16   15,13   11,10   7,7
16,16   12,12   8,8     4,4

Starting from the top left node we search for the seaarch space such that 
g(x)>=g'(x)+hmin(x) g' cost of reaching to the node. hmin minimum cost to reach the goal from the node

g(x)<=g'(x)+hmax(x) g' cost of reaching to the node. hmax maximum cost to reach the goal from the node

The algorithm is complete and generates optimal solution
"""
m,n = 0,0 # global parameter for grid space n rows m columns
l = [] #list to note the possible solution space

def heuristic(i,j):
    """
    Lower bound heuristics
    params
    i: row index
    j: column index

    """
    return i*(m-j+1)+((n*(n+1)//2) - (i*(i+1)//2))
def max_heuristic(i,j):
    """
    upper bound heuristics
    params:
    i: row index
    j: column index
    """
    return ((n*(n+1)//2) - (i*(i+1)//2))+(m-j)*n

def matrix():
    """
    Auxillary function of printing matrix
    """
    global m,n
    for i in range(m):
        for j in range(n):
            print(i+1,end=" ")
        print()
    for i in range(m):
        for j in range(n):
            print(heuristic(i+1,j+1),end=" ")
        print() 

def get_content(pos,p,c,op):
    """
    Function to generate the next path and associated paths for the next path taken
    params:
    pos: initial i,j index
    p: path string, identifying the path to the current node
    c: cost representing the sum of paths till the current node
    op: character specifying either Right or Down operation
    """
    path = p
    cost = c
    i,j = pos
    if op=='R':
        j+=1
        path= path +'R'
        cost+=i
    if op=='D':
        i+=1
        path= path+'D'
        cost+=i
    return {'pos':(i,j),'path':path,'cost':cost}
      
def moveValid(pos,current_cost,final_cost):
    """
    Generates the list of possible path from the current node
    params: 
    pos: current position
    current_cost: cost till the current node
    final_cost: the goal which needs to be achieved 
    """
    
    i,j = pos
    moves=[]
    #checking if the next move is under the minimum and maximum heuristics
    if final_cost>=(current_cost+heuristic(i,j+1)) and (final_cost-current_cost-i)<=max_heuristic(i,j+1) and (j+1)<=m:
        moves.append('R')
    if final_cost>=(current_cost+heuristic(i+1,j)) and (final_cost-current_cost-(i+1))<=max_heuristic(i+1,j)  and (i+1)<=n:
        moves.append('D') 
    return moves       


def findgoal(cost,w):
    """
    Starting from the left most element the approach calculates the possible path
    params: 
    cost: specifying the goal 
    w: file where the results are written
    """
    #Intialization
    index =0 
    initial_cost = 1 #initialization with one for every node
    list_open={} #maintaining the active number of search nodes
    i,j = 1,1
    #solution=[]
    list_open=[] 
    list_open.append({'pos':(i,j),'path':'','cost':initial_cost})
    #Path finding
    while True:
        #If all solution spaces are been visited and no new node needs to be explore all possible solutions are obtained
        if len(list_open)==0 or index>100:
            return ""
        l = list_open.pop()
        #Last node is reached with specific cost written to the file
        if l['pos']==(n,m) and l['cost']==cost:
            w.write(str(l['path'])+", ")
            index+=1
        #Possible moves are found and updated    
        else:    
            moves = moveValid(l['pos'],l['cost'],cost)
            if len(moves)!=0:
                for move in moves:
                    content = get_content(l['pos'],l['path'],l['cost'],move)
                    list_open.append(content)
       
    
#1 a
w=open("output_question_1","w")
n = 9 
m = 9
cost = 65
w.write(str(cost)+" ")
findgoal(cost,w)
w.write("\n")
cost = 72
w.write(str(cost)+" ")
findgoal(cost,w)
w.write("\n")
cost = 90
w.write(str(cost)+" ")
findgoal(cost,w)
w.write("\n")
cost = 110
w.write(str(cost)+" ")
findgoal(cost,w)
w.write("\n")
w.write("\n")

#1 b
n = 90000
m = 100000
cost = 87127231192
w.write(str(cost)+" ")
findgoal(cost,w)
w.write("\n")

cost = 5994891682
w.write(str(cost)+" ")
findgoal(cost,w)
w.write("\n")

w.close()