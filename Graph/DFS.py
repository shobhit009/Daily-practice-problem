def DFSRec (adj_list,s,visited):
    visited[s] = True
    print (s)
    for ele in adj_list[s]:
        if visited[ele] ==False:
            DFSRec(adj_list,ele,visited)

def DFS(adj_list,v,s):
    visited = [False]*v
    DFSRec(adj_list,s,visited)

if __name__ == "__main__":
    adj_list = {0:[1,4],1:[0,2],2:[1,3],3:[2],4:[0,5,6],5:[4,6],6:[4,5]}
    v = 7
    s = 0
    DFS(adj_list,v,s)
