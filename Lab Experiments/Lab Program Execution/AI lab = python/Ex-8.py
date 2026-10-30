def alphabeta(tree, alpha, beta, maximizing):
    if isinstance(tree, int):
        return tree

    if maximizing:
        value = float('-inf')
        for x in tree:
            value = max(value, alphabeta(x, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for x in tree:
            value = min(value, alphabeta(x, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

tree = [[3, 5], [2, 9]]
print("Best Value:", alphabeta(tree, float('-inf'),
                               float('inf'), True))
