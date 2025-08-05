colors = ['Red', 'Green', 'Blue']
regions = ['A', 'B', 'C']
adjacent = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}

def assign_color(assignment):
    if len(assignment) == len(regions):
        return assignment
    region = [r for r in regions if r not in assignment][0]
    for color in colors:
        if all(assignment.get(nei) != color for nei in adjacent[region]):
            assignment[region] = color
            result = assign_color(assignment)
            if result:
                return result
            del assignment[region]
    return None

print(assign_color({}))
