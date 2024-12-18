
def open_file():
    filepath = "day10/input.txt"
    file = open(filepath, "r")
    return file

def get_map_from_file(file):
    input_text = ""
    for line in file:
        input_text += line
    topo_map = [list(map(int, line.strip())) for line in input_text.strip().split('\n')]
    file.close()
    return topo_map

def get_map_from_file_2(file):
    topo_map = []
    for line in file:
        topo_map.append(list(map(int, line.strip())))
    return topo_map

def iterate_through_trailheads(topo_map):
    trailhead_scores = 0
    for y in range(len(topo_map)):
        for x in range(len(topo_map[y])):
            if topo_map[x][y] == 0:
                #do depth first search
                visited = set()
                reachable = depth_first_search(topo_map, x, y, visited, 0)
                trailhead_scores += len(reachable)
    return trailhead_scores

def depth_first_search(topo_map, x, y, visited, cur_height):
    rows = len(topo_map)
    columns = len(topo_map[0])
    if 0 > x or x >= rows or 0 > y or y >= columns:
        return set()
    cur_loc = (x, y)
    if cur_loc in visited:
        return set()
    if topo_map[x][y] != cur_height:
        return set()

    visited.add(cur_loc)

    reachable = set()

    if topo_map[x][y] == 9:
        reachable.add(cur_loc)
        return reachable

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        reachable |= depth_first_search(topo_map, new_x, new_y, visited, cur_height + 1)
    return reachable



def iterate_through_trailheads_2(topo_map):
    rating_sum = 0
    for y in range(len(topo_map)):
        for x in range(len(topo_map[y])):
            if topo_map[x][y] == 0:
                visited = set()
                rating_sum += depth_first_search_paths(topo_map, x, y, visited, 0)
    return rating_sum

def depth_first_search_paths(topo_map, x, y, visited, cur_height):
    rows = len(topo_map)
    columns = len(topo_map[0])
    if 0 > x or x >= rows or 0 > y or y >= columns:
        return set()
    cur_loc = (x, y)
    if cur_loc in visited:
        return set()
    if topo_map[x][y] != cur_height:
        return set()
    
    visited.add(cur_loc)

    if topo_map[x][y] == 9:
        visited.remove(cur_loc) #backtracking
        return 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    total_paths = 0
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        path_list = depth_first_search_paths(topo_map, new_x, new_y, visited, cur_height + 1)
        print(type(path_list))
        total_paths += len(path_list)
    visited.remove((x, y))  # Backtrack
    return total_paths



#setting stuff up
file = open_file()
topo_map = get_map_from_file(file)
#print(*topo_map)
trailhead_scores = iterate_through_trailheads(topo_map)
print(f"Total score for part 1: {trailhead_scores}")


"""
Unfortunately, after hours of trying, I could not figure out part 2 on my own and 
went to a youtube video (bradley sward) for help, and it was very useful
"""

def get_element_value(array, y, x):
    return -1 if y < 0 or x < 0 or y >= len(array) or x >= len(array) else array[y][x]
with open("day10/input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    for index, line in enumerate(lines):
        lines[index] = [int(x) for x in line]

    total = 0
    total_paths = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if get_element_value(lines, y, x) == 0:
                check = [[y, x, 0]]
                found = set()
                found_list = []
                while len(check) > 0:
                    if check[0][2] == 9:
                        found.add(tuple(check[0]))
                        found_list.append(check[0])
                    else:
                        if get_element_value(lines, check[0][0]+1, check[0][1]) == check[0][2]+1:
                            check.append([check[0][0]+1, check[0][1], check[0][2]+1])
                        if get_element_value(lines, check[0][0], check[0][1]+1) == check[0][2]+1:
                            check.append([check[0][0], check[0][1]+1, check[0][2]+1])
                        if get_element_value(lines, check[0][0]-1, check[0][1]) == check[0][2]+1:
                            check.append([check[0][0]-1, check[0][1], check[0][2]+1])
                        if get_element_value(lines, check[0][0], check[0][1]-1) == check[0][2]+1:
                            check.append([check[0][0], check[0][1]-1, check[0][2]+1])
                    del(check[0])
                total += len(found)
                total_paths += len(found_list)
    #print(f"total score for part 1: {total}")
    print(f"Total score for part 2: {total_paths}")


"""
Overall a good problem that really exposed my weakness when it comes to dynamic programming and graphs
I know what I need to work on now

"""
















