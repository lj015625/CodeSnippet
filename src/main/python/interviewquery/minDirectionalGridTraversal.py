"""
You are given the layout of a rectangular building with rooms forming a grid. Each room has four doors to the room to the north, east, south, and west where exactly one door is unlocked and the other three doors are locked. In each time step, you can move to an adjacent room via an unlocked door.

Your task is to determine the minimum number of time steps required to get from the northwest corner to the southeast corner of the building.

Note: if the path doesn’t lead you to exit return -1 .

The input is given as:

a non-empty 2d-array of letters 'N’, 'E’, ’S’, 'W’ named 'building’
'building[0][0]’ represents the open door at the northwest corner.
The rows of this array are associated with north-south direction.
The columns are associated with east-west direction.
"""


def minimum_direction(path_map):
    row = 0
    col = 0
    count = 0
    grid_size = len(path_map)
    while True:
        # invalid
        if row >= grid_size or col >= grid_size or path_map[row][col] == 0:
            return -1

        # reached final step
        if row == grid_size - 1 and col == grid_size - 1:
            return count

        if path_map[row][col] == "E":
            path_map[row][col] = 0
            col += 1
            count += 1

        elif path_map[row][col] == "W":
            path_map[row][col] = 0
            col -= 1
            count += 1

        elif path_map[row][col] == "N":
            path_map[row][col] = 0
            row -= 1
            count += 1

        elif path_map[row][col] == "S":
            path_map[row][col] = 0
            row += 1
            count += 1

        else:
            return -1


a = [['E', 'E', 'S', 'W'],  # row 1
     ['N', 'W', 'S', 'N'],  # row 2
     ['S', 'E', 'E', 'S'],  # row 3
     ['E', 'N', 'W', 'W']]  # row 4
print(minimum_direction(a))
