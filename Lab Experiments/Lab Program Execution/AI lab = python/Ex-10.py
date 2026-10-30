def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(source, "->", target)
        return

    hanoi(n-1, source, target, auxiliary)
    print(source, "->", target)
    hanoi(n-1, auxiliary, source, target)

hanoi(3, 'A', 'B', 'C')
