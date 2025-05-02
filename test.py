def spiralize_00(size):
    # Initialize the board with zeros
    board = [[0 for _ in range(size)] for _ in range(size)]

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = y = dir_idx = 0

    def is_valid(ny, nx):
        # Check if inside the board and if the cell is 0
        if 0 <= ny < size and 0 <= nx < size and board[ny][nx] == 0:
            # Check all 8 surrounding cells
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    ty, tx = ny + dy, nx + dx
                    if 0 <= ty < size and 0 <= tx < size:
                        if board[ty][tx] == 1:
                            return False
            return True
        return False

    while True:
        board[y][x] = 1
        dy, dx = directions[dir_idx]
        ny, nx = y + dy, x + dx
        if is_valid(ny, nx):
            y, x = ny, nx
        else:
            # try to turn right
            dir_idx = (dir_idx + 1) % 4
            dy, dx = directions[dir_idx]
            ny, nx = y + dy, x + dx
            if is_valid(ny, nx):
                y, x = ny, nx
            else:
                break
            
    return board

def test(func):    
    test_cases = [
        (5, [[1,1,1,1,1],
             [0,0,0,0,1],
             [1,1,1,0,1],
             [1,0,0,0,1],
             [1,1,1,1,1]]),
        
        (8, [[1,1,1,1,1,1,1,1],
             [0,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,0,1],
             [1,0,0,0,0,1,0,1],
             [1,0,1,0,0,1,0,1],
             [1,0,1,1,1,1,0,1],
             [1,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,1,1]]),
    ]

    print(f"\nTesting {func.__name__}:")
    print("-" * 30)  # Separator line
    for a, expected in test_cases:
        result = func(a)
        print(f"\nFunc: {func.__name__}({a})\n  Result: {result}\nExpected: {expected}")
    print("-" * 30)  # End separator line

# Run tests for each version
test(spiralize_00)
#test(spiralize_01)
#test(spiralize_02)