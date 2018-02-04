# Head begins here
ROBOT = 'm'
PRINCESS = 'p'

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

def find(item, grid):
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == item:
                return (x, y)

def horizontal_moves(distance):
    return [RIGHT] * distance if distance > 0 else [LEFT] * (-distance)

def vertical_moves(distance):
    return [DOWN] * distance if distance > 0 else [UP] * (-distance)

def path_between(from_square, to_square):
    from_x, from_y = from_square
    to_x, to_y = to_square
    return horizontal_moves(to_x - from_x) + vertical_moves(to_y - from_y)

def get_path_to_princess(grid):
    robot_square = find(ROBOT, grid)
    princess_square = find(PRINCESS, grid)
    return path_between(robot_square, princess_square):

# Tail begins here
size = input()

grid = []
for i in xrange(0, size):
    grid.append(raw_input().strip())

for move in get_path_to_princess(grid):
    print move
