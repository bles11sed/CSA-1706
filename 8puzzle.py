from collections import deque

goal_state = '123456780' 

def get_neighbors(state):
    neighbors = []
    i = state.index('0')
    moves = []

    if i >= 3: moves.append(i - 3)        
    if i <= 5: moves.append(i + 3)        
    if i % 3 != 0: moves.append(i - 1)    
    if i % 3 != 2: moves.append(i + 1)    

    for m in moves:
        new_state = list(state)
        new_state[i], new_state[m] = new_state[m], new_state[i]
        neighbors.append(''.join(new_state))
    return neighbors

def bfs(start):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))
    return None


start_state = '724506831' 

solution = bfs(start_state)
if solution:
    print("Steps to solve:")
    for s in solution:
        for i in range(0, 9, 3):
            print(s[i:i+3])
        print()
else:
    print("No solution found.")
