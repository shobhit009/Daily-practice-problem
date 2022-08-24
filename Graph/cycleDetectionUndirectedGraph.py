def detect_cycle(adj_list,v):
    visited = [False]*v
    for i in range(v):
        if visited[i] == False:
            if DFSRec(adj_list,visited,i,-1)==True:
                return True
    return False


def DFSRec(adj_list,visited,s,p):
    visited[s] = True
    for u in adj_list[s]:
        if visited[u] == False:
            if (DFSRec(adj_list,visited,u,s)) == True:
                return True
        elif u!=p:
            return True
        
    return False

if __name__ == "__main__":
    adj_list = {0:[1],1:[0,2],2:[1,3],3:[1,2]}
    v = 4
    print(detect_cycle(adj_list,v))
