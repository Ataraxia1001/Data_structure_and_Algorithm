import sys
from heapq import heapify, heappush, heappop

# youtube lecture: https://www.youtube.com/watch?v=OrJ004Wid4o

def dijkstra(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]}
    }
    node_data[src]['cost'] = 0
    visited = [] # all visited nodes
    temp = src   # temp: current node
    for i in range(5):   # 6 nodes in graph -> 6-1 = 5 steps(0,1,2,3,4)
        if temp not in visited: # TODO: Reassign source
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:   # if graph[temp]='A', then j='B','C'
                if j not in visited:  # j is already visited, don't calculate cost again.
                    cost = node_data[temp]['cost'] + graph[temp][j]   # cost is new cost by passing current node 
                    if cost < node_data[j]['cost']:  # if new cost is less than previous cost
                        node_data[j]['cost'] = cost  # update cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp] # pred is used to store path. if new path is found, update it.
                    heappush(min_heap,(node_data[j]['cost'],j)) 
        heapify(min_heap) # heapify creates min_heap by default. 
        temp = min_heap[0][1]   
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))


if __name__ == "__main__":
    graph = {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22,'E':1}
    }

    source = 'A'        # starting node
    destination = 'F'   # ending node
    dijkstra(graph,source,destination)
