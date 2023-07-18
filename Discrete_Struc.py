# PROJECT BY 
# SAIF ALI KHAN (21i-0649) 
# RAYYAN Ziaullah (21i-2951)
# USMAN ZAFAR (21i-0608)
# SECTION - E
#
# PROGRAM TO FIND STRONGLY CONNECTED COMPONENTS AND PRINT ITS MEMBERS + SIZE OF GROUP

import sys # RAYYAN

limit = sys.getrecursionlimit()
  
# Print the current limit 
print('Before changing, limit of stack =', limit) #1000
  
# New limit
Newlimit = 10000
  
# Using sys.setrecursionlimit() method 
sys.setrecursionlimit(Newlimit) 
  
# Using sys.getrecursionlimit() method 
# to find the current recursion limit
limit = sys.getrecursionlimit()
  
# Print the current limit 
print('After changing, limit of stack =', limit) 

Adj_List = {} #dictionary

with open("datasheet.txt", mode='r') as fi:
    for line in fi:
        parts = line.split() # split first and 2nd colum
        Adj_List.setdefault(parts[0],[]).append(parts[1])
         # for directed 


#---------------------------------------------------------------------- SAIF
key_list = Adj_List.keys() # gets key list

add = [] # list that contains leaf nodes

for x, y in Adj_List.items(): 
    for z in y:
        if z not in key_list:     
            add.append(z)
for m in add:
    Adj_List.update({m:[]}) # leaf nodes have no further childs
#-----------------------------------------------------------------------

#------------------------------------------------- #RAYYAN
# now reverse edges Direction
R_Adj_List = {}
with open("datasheet.txt", mode='r') as f:
    for line in f:
        parts = line.split()
        R_Adj_List.setdefault(parts[1],[]).append(parts[0])

#-------------------------------------------------- SAIF
R_key_list = R_Adj_List.keys() # gets key list
R_add = [] # list that contains leaf nodes
for x, y in R_Adj_List.items(): 
    for z in y:
        if z not in R_key_list:     
            R_add.append(z)
for m in R_add:
    R_Adj_List.update({m:[]}) # leaf nodes have no further childs


#---------------------------------------------------------------------- SAIF
Color = {} # Keeps track of visited and unvisted Nodes, White = Not Visited, Gray = First explored , black = fully Explored
Parent = {} # Keeps Track of Parent Of Each Vertex
Traversal_time = {} # [start,end] OR [gray,Black] keeps track of when a node was first visited and when it was completely visited
DFS_OUTPUT = []

#initialize above array and Dictionary
for node in Adj_List.keys(): # the keys() function returns A view object that displays all the keys. 
    Color[node] = "W" # Set All Nodes To Univisited, That is make Color White
    Parent[node] = None # unvisited Nodes Have uninitalized Parent i.e None
    Traversal_time[node] = [-1, -1] # if a node is unvisited Set its inital values to -1,-1
# DFS algorithm

time = 0 # varaible that keeps track of time of a node visited
def DFS(u): # pass the initial argument u which is starting node
    global time # Set the Varaible global so that we can Modify the variable outside of the current scope

    Color[u] = "G" # visited 
    Traversal_time[u][0] = time # Setting the Starting Time for the Vertex u    if visited is None:
    if u not in DFS_OUTPUT:
        DFS_OUTPUT.append(u) # Add u node to output list
    # Now we need to iterate over all the adjacent vertices of u
    time +=1
    for v in Adj_List[u]:
        # First Check if Vertex is Visted or not by its Color
        if Color[v] == "W": # if Color of vertex is white then it means that it is not visited 
            Parent[v] = u # if the child vertex of u was unvisted then make its parent as u
            DFS(v) # recursively call the DFS for the V vertex Now which is unvisited

    # After Exploring All the Vertices Are of U , Now Set it to Black
    Color[u] = "B" # fully Explored u
    Traversal_time[u][1] = time # after u has been fully visited set its final time
    time += 1 #increment time varaible by 1

#---------------------------------------------------------------------------------------REVERSE DFS
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

R_Color = {} # Keeps track of visited and unvisted Nodes, White = Not Visited, Gray = First explored , black = fully Explored
R_Parent = {} # Keeps Track of Parent Of Each Vertex
R_Traversal_time = {} # [start,end] OR [gray,Black] keeps track of when a node was first visited and when it was completely visited
R_DFS_OUTPUT = [] 

#initialize above array and Dictionary
for node in R_Adj_List.keys(): # the keys() function returns A view object that displays all the keys. 
    R_Color[node] = "W" # Set All Nodes To Univisited, That is make Color White
    R_Parent[node] = None # unvisited Nodes Have uninitalized Parent i.e None
    R_Traversal_time[node] = [-1, -1] # if a node is unvisited Set its inital values to -1,-1
# DFS algorithm
R_time = 0 # varaible that keeps track of time of a node visited
def R_DFS(u): # pass the initial argument u which is starting node
    global R_time # Set the Varaible global so that we can Modify the variable outside of the current scope

    R_Color[u] = "G"
    R_Traversal_time[u][0] = R_time # Setting the Starting Time for the Vertex u    if visited is None:

    if u not in R_DFS_OUTPUT:
        R_DFS_OUTPUT.append(u) # Add u node to output list
    # Now we need to iterate over all the adjacent vertices of u
    R_time +=1
    for v in R_Adj_List[u]:
        # First Check if Vertex is Visted or not by its Color
        if R_Color[v] == "W": # if Color of vertex is white then it means that it is not visited 
            R_Parent[v] = u # if the child vertex of u was unvisted then make its parent as u
            R_DFS(v) # recursively call the DFS for the V vertex Now which is unvisited

    # After Exploring All the Vertices Are of U , Now Set it to Black
    R_Color[u] = "B" # fully Explored u
    R_Traversal_time[u][1] = R_time # after u has been fully visited set its final time
    R_time += 1 #increment time varaible by 1


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#---------------------------------------------------------------------------------------
print("NORMAL DFS STARTED")
#DFS('0') # start the DFS Algorithm with 0 root vertex, NOTE : Right now only works for a graph that is fully connected 
print("REVERSE DFS STARTED")
#R_DFS('5')

SCC_NODES = [] # RAYYAN PART

for x, y in Adj_List.items():
     #print("KEY: ",x)
     DFS(x) 
     #print (DFS_OUTPUT) #print
     #print("-----------------------")

     #print("REVERSE")
     #print("KEY: ",x)
     R_DFS(x) 
     #print(R_DFS_OUTPUT)
     #print("-----------------------")

     length_DFS = len(DFS_OUTPUT) # get lenth of array 
     length_RDFS = len(R_DFS_OUTPUT) 

     if length_DFS == length_RDFS: # if both the arrays match then add node to SCC
         SCC_NODES.append(x)
#---------------------------------------------------------------------------------------


#print (DFS_OUTPUT) #print
#print("-----------------------")
#print(R_DFS_OUTPUT)
#print("-----------------------")
#print (Parent)

#print (Traversal_time) instead of printing it like this , use the below loop
#print("@@@@@@@@@@@@")
#for vertex in Adj_List.keys():
#    print(vertex, " -> ", Traversal_time[vertex]) # prints the traversal time of each node line by line
#print("------------------------")

#for R_vertex in R_Adj_List.keys():
#    print(R_vertex, " -> ", R_Traversal_time[R_vertex]) # prints the traversal time of each node line by line

print("SCC:")
print("NODES:")
print(SCC_NODES) 
print("SCC LENGTH:")
print(len(SCC_NODES)) 

