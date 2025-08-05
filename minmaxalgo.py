def minimax(depth, is_max):
    if depth == 0:
        return 1 if is_max else -1
    scores = [minimax(depth-1, not is_max) for _ in range(2)]
    return max(scores) if is_max else min(scores)

print("Minimax Value:", minimax(3, True))
