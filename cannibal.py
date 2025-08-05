def is_valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c)

def solve():
    from collections import deque
    visited = set()
    queue = deque([((3, 3, 1), [])])  

    while queue:
        state, path = queue.popleft()
        if state[:2] == (0, 0):
            print("Steps:")
            for p in path + [state]:
                print(p)
            return
        if state in visited:
            continue
        visited.add(state)
        m, c, b = state
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        for dm, dc in moves:
            if b == 1:
                new = (m-dm, c-dc, 0)
                back = (3-m+dm, 3-c+dc, 1)
            else:
                new = (m+dm, c+dc, 1)
                back = (3-m-dm, 3-c-dc, 0)
            if is_valid(*new[:2]) and is_valid(3-new[0], 3-new[1]):
                queue.append((new, path + [state]))
solve()
