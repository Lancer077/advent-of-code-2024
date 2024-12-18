
filepath = "day06/input.txt"
file = open(filepath, "r")


"""
There is a guard that will always walk forward, unless there is an object 
in the way, in which case the guard will take a 90* turn to the right
we want to count how many unique spaces the guard visits

"""

def check_out_of_bounds(guard_map, cur_guard_x, cur_guard_y, cur_guard_direction, direction_offsets_x, direction_offsets_y) -> bool:
    x_max = len(guard_map[0])-1
    y_max = len(guard_map)-1
    if cur_guard_x + direction_offsets_x[cur_guard_direction] < 0:
        return True
    if cur_guard_y + direction_offsets_y[cur_guard_direction] < 0:
        return True
    if cur_guard_x + direction_offsets_x[cur_guard_direction] > x_max:
        return True
    if cur_guard_y + direction_offsets_y[cur_guard_direction] > y_max:
        return True
    return False


def update_coords_and_direction(guard_map, cur_x_coord, cur_y_coord, cur_guard_direction):
    new_x_coord = cur_x_coord + direction_offsets_x[cur_guard_direction]
    new_y_coord = cur_y_coord + direction_offsets_y[cur_guard_direction]
    if guard_map[new_y_coord][new_x_coord] == "#":
        cur_guard_direction += 1
        cur_guard_direction %= 4
        return cur_x_coord, cur_y_coord, cur_guard_direction

    return new_x_coord, new_y_coord, cur_guard_direction


cur_guard_direction = 0
direction_offsets_x = [0, 1, 0, -1]
direction_offsets_y = [-1, 0, 1, 0]
cur_guard_x = -1
cur_guard_y = -1

guard_map = []
line_counter = 0
guard_starting_x_coord = -1
guard_starting_y_coord = -1

for line in file:
    guard_map.append(line)
    if "^" in line:
        cur_guard_y = line_counter
        cur_guard_x = line.index("^")
        guard_starting_x_coord = cur_guard_x
        guard_starting_y_coord = cur_guard_y
    line_counter+=1

distinct_positions = set()

while not check_out_of_bounds(guard_map, cur_guard_x, cur_guard_y, cur_guard_direction, direction_offsets_x, direction_offsets_y):
    distinct_positions.add((cur_guard_x, cur_guard_y))
    cur_guard_x, cur_guard_y, cur_guard_direction = update_coords_and_direction(guard_map, cur_guard_x, cur_guard_y, cur_guard_direction)

print(f"Total unique positions {len(distinct_positions)}")

"""
alright I don't think that one was too bad, lets move on to part b
he said, knowing damn well it took about 2 hours because tuples were being weird

Now onto part 2 and we are trying to find all the ways where placing one obstruction would get the guard stuck in an infinite loop
I will loop through all the locations that are currently filled with "." and then run the simulation 
I will check for the infinite loop by creating a set of type list which will hold the x coord, y coord, and the corresponding guard direction number
If at any point those 3 match up, we know we are in a looping state
If we exit the boundaries first, we know we are NOT in a looping state
Not a half bad idea
"""
guard_map_2 = []
for line in guard_map:
    line = line.replace("\n", "")
    guard_map_2.append(line)



def test_map_copy(guard_map):
    x_pos = guard_starting_x_coord
    y_pos = guard_starting_y_coord
    cur_dir = 0
    direction_offsets_x = [0, 1, 0, -1]
    direction_offsets_y = [-1, 0, 1, 0]
    for i in range(10000):
        #print(f"X: {x_pos}, Y: {y_pos}")
        if check_out_of_bounds(guard_map, x_pos, y_pos, cur_dir, direction_offsets_x, direction_offsets_y):
            return 0
        x_pos, y_pos, cur_dir = update_coords_and_direction(guard_map, x_pos, y_pos, cur_dir)
    return 1


def test_loop():
    total = 0
    for y in range(len(guard_map_2)):
        for x in range(len(guard_map_2)):
            map_copy = guard_map.copy()
            if map_copy[y][x] == ".":
                line = map_copy[y]
                line = line[:x] + "#" + line[1+x:]
                map_copy[y] = line
                total += test_map_copy(map_copy)
                
    print(total)


test_loop()




"""
I have spend an ungodly number of hours on this problem just to realize a function was not being passed
in the updated map and was instead using the originally created one
I feel so incredibly stupid
but also that's just what happens when you use global variables
you pay the price of being lazy
regardless, I am very happy to put this one behind me

"""