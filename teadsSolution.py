import sys, math
import collections
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of adjacency relations
graph = collections.defaultdict(lambda: list())
linkList = list()

for i in xrange(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(i) for i in raw_input().split()]
    linkList.append((xi, yi))

for link in linkList:
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])

counter=0

while len(graph)>1:
    counter+=1
    leaves=[]
    for node in graph:
        if len(graph[node])==1:
            leaves.append(node)
    
    for leave in leaves:
        if len(graph)<>1:
            adjLeave=graph[leave][0]
            del graph[leave]
            adjList=graph[adjLeave]
            adjList.remove(leave)
        else:
            del graph[leave]
            
print counter
        
