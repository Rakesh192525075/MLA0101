def minimax(tree, maximizing):
    if isinstance(tree, int):
        return tree

    values = [minimax(x, not maximizing) for x in tree]

    if maximizing:
        return max(values)
    return min(values)

tree = [[3, 5], [2, 9]]

print("Best Value:", minimax(tree, True))
