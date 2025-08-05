def pour(from_cap, to_cap, target):
    from_jug = from_cap
    to_jug = 0

    steps = [(from_jug, to_jug)]

    while from_jug != target and to_jug != target:
        # Find the maximum amount that can be poured
        pour_amount = min(from_jug, to_cap - to_jug)

        # Pour water
        to_jug += pour_amount
        from_jug -= pour_amount
        steps.append((from_jug, to_jug))

        # Check if we reached the target
        if from_jug == target or to_jug == target:
            break

        # If from_jug is empty, refill it
        if from_jug == 0:
            from_jug = from_cap
            steps.append((from_jug, to_jug))

        # If to_jug is full, empty it
        if to_jug == to_cap:
            to_jug = 0
            steps.append((from_jug, to_jug))

    print("Steps to get", target, "liters:")
    for step in steps:
        print("Jug1:", step[0], "Jug2:", step[1])

# Example: Jug1 = 4L, Jug2 = 3L, target = 2L
pour(4, 3, 2)
