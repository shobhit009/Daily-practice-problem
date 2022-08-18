#version1 - Given undirected graph, source given

# def BFS(adj_list, v, s):
#     q = []
#     visited = [False]*v
#     q.append(s)
#     visited[s] = True

#     while (len(q)):
#         curr = q.pop(0)
#         print (curr)

#         for ele in adj_list[curr]:
#             if visited[ele] == False:
#                 visited[ele] = True
#                 q.append(ele)

# if __name__ == "__main__":
#     adj_list = {0:[1,2],1:[0,2,3],2:[0,1,3,4],3:[1,2,4],4:[2,3]}
#     v = 5
#     s = 0
#     BFS(adj_list,v,s)

# Version 2 - Given undirected disconnected graph , source not given
def BFS(adj_list, v, s, visited):
    q = []
    q.append(s)
    visited[s] = True

    while (len(q)):
        curr = q.pop(0)
        print (curr)

        for ele in adj_list[curr]:
            if visited[ele] == False:
                visited[ele] = True
                q.append(ele)

def BFSDis(adj_list,v):
    visited = [False]*v  

    for i in range(v):
        if visited[i] == False:
            BFS(adj_list,v,i,visited)

if __name__ == "__main__":
    adj_list = {0:[1,2],1:[0,3],2:[0,3],3:[1,2],4:[5,6],5:[4,6],6:[4,5]}
    v = 7
    s = 0
    BFSDis(adj_list,v)
