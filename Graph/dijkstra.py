def getMinNode(distance,visited):
    min = float('inf')
    v = len(distance)
    for i  in range(v):
        if visited[i] == False:
            if distance[i] < min:
                min = distance[i]
                index = i
    return index
 
def findSingleSourceShortestPath(adj_matrix,v):
    INT_MAX = float('inf')
    visited = [False]*v
    distance = [INT_MAX]*v
    parent = [None]*v

    # initializing parent and weight for the source node
    distance[0] = 0
    parent[0] = -1

    for i in range(v):
        u = getMinNode(distance,visited)
        visited[u] = True

        # 3 constraints
        # for each j there should be an edge connecting between u and j through an intermediate node
        # j should not be visited already
        # if cost to reach j directly from u is greater than the cost to reach j via intermediate node , then we will update 
        # the cost

        for j in range(v):
            if (adj_matrix[u][j] != 0 and visited[j] == False and distance[u]+adj_matrix[u][j] < distance[j]):
                distance[j] = distance[u]+adj_matrix[u][j]
                parent[j] = u

    for i in range(1,v):
        print(parent[i],"-",i,"\t",distance[i])

if __name__ == "__main__":
    adj_mat = [[0,1,0,4],
                  [1,0,2,5],
                  [0,2,0,3],
                  [4,5,3,0]]
    vertex = 4

    findSingleSourceShortestPath(adj_mat,vertex)