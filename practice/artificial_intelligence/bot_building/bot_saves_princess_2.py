PRINCESS = 'p'

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

def find_princess(grid):
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == PRINCESS:
                return (x, y)

def get_next_move_towards_princess(robot_square, grid):
    robot_x, robot_y = robot_square
    princess_x, princess_y = find_princess(grid)

    if robot_x < princess_x:
        return RIGHT
    elif robot_x > princess_x:
        return LEFT
    elif robot_y < princess_y:
        return DOWN
    elif robot_y > princess_y:
        return UP

def main():
    size = input()
    robot_y, robot_x = [int(i) for i in raw_input().strip().split()]
    grid = [[j for j in raw_input().strip()] for i in xrange(size)]

    print get_next_move_towards_princess((robot_x, robot_y), grid)

if __name__ == "__main__":
    main()