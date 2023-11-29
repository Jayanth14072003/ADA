def bfs(graph,start,path):
 q=[start]
 path.append(start)
 while q:
  node=q.pop(0)
  for v in graph[node]:
     if not v in path:
      path.append(v)
      q.append(v)
def dfs(graph,node,path):
    path.append(node)
    for v in graph[node]:
        if v not in path:
            dfs(graph,v,path)
graph={'A':['B','C'], 'B':['E','G'], 'C':['F'], 'D':['A','B','C','E'], 'E':['F','D'], 'F':[], 'G':['E','F']}
dfs_path=[]
bfs_path=[]
dfs(graph,'A',dfs_path)
bfs(graph,'A',bfs_path)
print("DFS travel path:",dfs_path)
print("BFS travel path:",bfs_path)
