def vacuum(state):
    for i in range(2):
        if state[i] == 1:
            print(f"Cleaning Room {i}")
            state[i] = 0
    print("Done. State:", state)

vacuum([1, 1])  
