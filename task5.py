with open('Input/input5.txt') as f:
    lines = f.read().splitlines()


def get_direction(from_to):
    from_xy_tmp, to_xy_tmp = from_to.split(' -> ')
    from_xy = dict(zip(['x', 'y'], tuple(int(x) for x in from_xy_tmp.split(','))))
    to_xy = dict(zip(['x', 'y'], tuple(int(x) for x in to_xy_tmp.split(','))))
    return {'from': from_xy, 'to': to_xy}


sign = lambda x: (x > 0) - (x < 0)


def move(visited, step_direction):
    x_from, y_from = step_direction['from']['x'], step_direction['from']['y']
    x_to, y_to = step_direction['to']['x'], step_direction['to']['y']

    # get direction
    x_move, y_move = sign(x_to - x_from), sign(y_to - y_from)

    # get difference for move
    diff = max(abs((x_to - x_from) * x_move), abs((y_to - y_from) * y_move))

    # move step by step
    x_current, y_current = x_from, y_from
    for i in range(diff+1):
        tmp = visited.get((x_current, y_current), 0) + 1
        visited[(x_current, y_current)] = tmp
        x_current, y_current = x_current + x_move, y_current + y_move

    return visited


def is_not_diagonal(step_direction):
    same_x = step_direction['from']['x'] == step_direction['to']['x']
    same_y = step_direction['from']['y'] == step_direction['to']['y']
    return same_x or same_y


visited1, visited2 = {}, {}
for step in range(0, len(lines)):
    step_direction = get_direction(from_to=lines[step])
    if is_not_diagonal(step_direction):
        visited1 = move(visited1, step_direction)
    visited2 = move(visited2, step_direction)

print(len([i for i in visited1.values() if i > 1]))
print(len([i for i in visited2.values() if i > 1]))
