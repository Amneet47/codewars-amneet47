# https://www.codewars.com/kata/58f6e7e455d7597dcc000045

def get_password(grid, directions):
    password = ""
    row_x = 0
    col_x = 0
    for row_index, row in enumerate(grid):
        for col_index, element in enumerate(row):
            if element == "x":
                row_x = row_index
                col_x = col_index
            break
        
    for direct in directions:
        if "down" in direct:
            row_x += 1
            if direct.endswith("T"):
                password += grid[row_x][col_x]
        elif "up" in direct:
            row_x -= 1
            if direct.endswith("T"):
                password += grid[row_x][col_x]
        elif "right" in direct:
            col_x += 1 
            if direct.endswith("T"):
                password += grid[row_x][col_x]
        elif "left" in direct:
            col_x -= 1 
            if direct.endswith("T"):
                password += grid[row_x][col_x]
                
    return password

print(get_password([["x", "l", "m"], ["o", "f", "c"], ["k", "i", "t"]], ["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"]))

# def get_password(grid, directions):
#     """
#     Retrieves a password from a grid based on movement directions.

#     Args:
#         grid: A 2D list representing the grid.
#         directions: A list of movement directions.

#     Returns:
#         The generated password string.
#     """

#     row_x, col_x = find_start_position(grid)
#     password = process_directions(grid, directions, row_x, col_x)
#     return password

# def find_start_position(grid):
#     """Finds the starting position ('x') in the grid."""
#     for row_index, row in enumerate(grid):
#         for col_index, element in enumerate(row):
#             if element == "x":
#                 return row_index, col_index
#     return 0, 0 #Default to 0,0 if x is not found.

# def process_directions(grid, directions, row_x, col_x):
#     """Processes movement directions and generates the password."""
#     password = ""
#     movement_map = {
#         "down": (1, 0),
#         "up": (-1, 0),
#         "right": (0, 1),
#         "left": (0, -1),
#     }

#     for direct in directions:
#         for move, (row_change, col_change) in movement_map.items():
#             if move in direct:
#                 row_x += row_change
#                 col_x += col_change
#                 if direct.endswith("T"):
#                     # Add bounds check
#                     if 0 <= row_x < len(grid) and 0 <= col_x < len(grid[0]):
#                         password += grid[row_x][col_x]
#                     else:
#                         print(f"Warning: Index out of bounds after direction: {direct}")
#                 break # break inner loop after finding direction.
#     return password