def alphabeta(depth, alpha, beta, is_max):
    if depth == 0:
        return 1 if is_max else -1
    if is_max:
        value = float('-inf')
        for _ in range(2):
            value = max(value, alphabeta(depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for _ in range(2):
            value = min(value, alphabeta(depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

print("Alpha-Beta Value:", alphabeta(3, float('-inf'), float('inf'), True))
