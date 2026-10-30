g = {'A':['B','C'], 'B':['D','E'],
     'C':['F'], 'D':[], 'E':[], 'F':[]}
def dfs(n):
    print(n, end=" ")
    for x in g[n]:
        if x not in visited:
            visited.append(x)
            dfs(x)
visited = ['A']
dfs('A')
