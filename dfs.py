graph={
    '15':['13','17'],
    '13':['12','14'],
    '17':['18'],
    '12':[],
    '14':['18'],
    '18':[]
}
visited=[]
def dfs(visited,grafh,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for nei in graph[node]:
            dfs(visited,graph,nei)
print("Following is the Depth first search")
dfs(visited,graph,'15')