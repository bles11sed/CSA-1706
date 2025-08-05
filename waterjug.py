def pour(from_cap, to_cap, target):
    from_jug = from_cap
    to_jug = 0

    steps = [(from_jug, to_jug)]

    while from_jug != target and to_jug != target:
        pour_amount = min(from_jug, to_cap - to_jug)

        to_jug += pour_amount
        from_jug -= pour_amount
        steps.append((from_jug, to_jug))

        if from_jug == target or to_jug == target:
            break

            if from_jug == 0:
            from_jug = from_cap
            steps.append((from_jug, to_jug))
        if to_jug == to_cap:
            to_jug = 0
            steps.append((from_jug, to_jug))

    print("Steps to get", target, "liters:")
    for step in steps:
        print("Jug1:", step[0], "Jug2:", step[1])

pour(4, 3, 2)
