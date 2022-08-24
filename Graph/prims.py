
def getMinNode(weight, setMST):
    v = len(weight)
    min = float('inf')
   
    for i in range(v):
        if (setMST[i] == False and weight[i] < min ):
            min = weight[i]
            vertex = i
         

    return vertex

def findMST(adj_mat,v):
    MAX_INF = float('inf')

    weight = [MAX_INF]*v
    parent = [None]*v
    setMST = [False]*v

    weight[0] = 0
    parent[0] = -1

    for i in range(v):
        u = getMinNode(weight,setMST)
        setMST[u] = True

        for j in range(v):
            # 3 constraints
            # there must be an edge between u(current selected node) and j(node to be found next)
            # J must not be included earlier
            # weight at J is greater than the edge connecting it to current node 
            if (adj_mat[u][j] != 0 and setMST[j] == False and adj_mat[u][j] < weight[j]):
                weight[j] = adj_mat[u][j]
                parent[j] = u

    for i in range(1, v):
            print(parent[i], "-", i, "\t", adj_mat[i][parent[i]])

if __name__ == "__main__":
    adj_mat = [[0,1,0,4],
                  [1,0,2,5],
                  [0,2,0,3],
                  [4,5,3,0]]
    vertex = 4

    findMST(adj_mat,vertex)