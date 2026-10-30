parent = {
    'Ravi': ['Arun', 'Priya'],
    'Arun': ['Kumar']
}

for p in parent:
    for child in parent[p]:
        print(p, "is parent of", child)

for p in parent:
    for child in parent[p]:
        if child in parent:
            for grandchild in parent[child]:
                print(p, "is grandparent of", grandchild)
