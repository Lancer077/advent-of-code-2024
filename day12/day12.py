

#reading the file in
def get_lines():
    #I figure a 2d matrix will be easier to deal with than a list of strings
    #although to be fair it'll probably be about the same
    filepath = "day12/input.txt"
    file = open(filepath, "r")
    lines = []
    for line in file:
        line = line.replace("\n", "")
        lines.append(list(line))
    file.close()
    return lines


"""
Current Plan:
Make a secondary 2d matrix with size lines_x + 1 and lines_y + 1
This secondary matrix will represent spaces in between the plants
We can start by filling the matrix with zeroes and putting a 1 wherever there needs to be
a fence
Then we can return that secondary matrix, and then call another function to get the overall price

"""

def print_matrix(matrix):
    for line in matrix:
        print(*line)
    print()
    
def get_fence_matrix(plants):
    fences = [[0 for _ in range((len(plants)*2)+1)] for _ in range(len((plants[0])*2)+1)]

    for y in range(len(plants)):
        for x in range(len(plants[y])):
            fences[(y*2)+1][(x*2)+1] = plants[y][x]
    #print_matrix(fences)


    #since the exterior will be filled with fences, we can just do that here
    for y in range(len(fences)):
        fences[y][0] = 1
        fences[y][len(fences[0])-1] = 1
    for x in range(len(fences[0])):
        fences[0][x] = 1
        fences[len(fences)-1][x] = 1

    #my brain struggles to understand this problem conceptually but I have the power jazz on my side so how could I lose
    prev_plant = plants[0][0]
    for y in range(len(plants)):
        for x in range(len(plants[y])):
            cur_plant = plants[y][x]
            if prev_plant != cur_plant:
                prev_plant = cur_plant
                fences[y*2+1][x*2] = 1

    prev_plant = plants[0][0]
    for x in range(len(plants[0])):
        for y in range(len(plants)):
            cur_plant = plants[y][x]
            if prev_plant != cur_plant:
                prev_plant = cur_plant
                fences[y*2][x*2+1] = 1
    
    
    #print_matrix(fences)
    return fences


def get_fencing_price(fences, plants):
    total_price = 0

    found_locations = set()
    for y in range(len(plants)):
        for x in range(len(plants[y])):
            cur_loc = (x*2+1, y*2+1)
            if cur_loc not in found_locations:
                found_locations.add(cur_loc)
                region_locations = set()
                already_checked = set()
                region_locations.add(cur_loc)
                region_perimiter = 0
                region_area = 0
                #loop through region locations
                while len(region_locations) > 0:
                    location = region_locations.pop()
                    if location not in already_checked:
                        already_checked.add(location)
                        region_area += 1
                        cur_x = location[0]
                        cur_y = location[1]
                        #print(f"Starting x: {cur_x} y: {cur_y}")
                        #set a directional thing
                        x_offsets = [ 0, 1, 0, -1]
                        y_offsets = [-1, 0, 1,  0]
                        for dir in range(4):
                            next_x = abs(cur_x + x_offsets[dir])
                            next_y = abs(cur_y + y_offsets[dir])
                            #print(next_x, next_y)
                            if fences[next_y][next_x] == 1:
                                region_perimiter += 1
                            else:
                                next_plant = (abs(next_x+x_offsets[dir]), abs(next_y+y_offsets[dir]))
                                region_locations.add(next_plant)
                                found_locations.add(next_plant)
                            #print(found_locations)
                    #print(f"Area: {region_area}")
                #print(already_checked)
                total_price += (region_area * region_perimiter)

    return total_price

def solve_part_1():
    plants = get_lines()
    fences = get_fence_matrix(plants)
    total_price = get_fencing_price(fences, plants)
    print(f"Total Price for part 1: {total_price}")



"""
YYEEEEESSSSSSSSSSSS!!!!!!!
Words cannot contain my excitement right now
I've been working on this for 1.5 hours, trying to figure out where I was getting bugs and questioning my whole approach
It feels really really good
and I know damn well part 2 will bring me back down to earth but right now I'm going to enjoy this feeling of satisfaction

Ok I'm good now lets get part 2

so we can get a bulk discount if perimeter sides are straight, this is probably going to suck
I figure I might be able to make use of the already checked set to find tuples but I'll have to see
But I got a different, slightly cheating idea I want to try first
"""

def get_fencing_price_2(fences, plants):
    total_price = 0
    found_locations = set()
    for y in range(len(plants)):
        for x in range(len(plants[y])):
            cur_loc = (x*2+1, y*2+1)
            if cur_loc not in found_locations:
                local_fences = fences.copy()
                local_fences = reset_fences(local_fences)
                found_locations.add(cur_loc)
                region_locations = set()
                already_checked = set()
                region_locations.add(cur_loc)
                region_perimiter = 0
                region_area = 0
                #loop through region locations
                while len(region_locations) > 0:
                    location = region_locations.pop()
                    if location not in already_checked:
                        already_checked.add(location)
                        region_area += 1
                        cur_x = location[0]
                        cur_y = location[1]
                        #print(f"Starting x: {cur_x} y: {cur_y}")
                        #set a directional thing
                        x_offsets = [ 0, 1, 0, -1]
                        y_offsets = [-1, 0, 1,  0]
                        for dir in range(4):
                            next_x = abs(cur_x + x_offsets[dir])
                            next_y = abs(cur_y + y_offsets[dir])
                            #print(next_x, next_y)
                            if next_y < len(local_fences) and next_x < len(local_fences[0]) and local_fences[next_y][next_x] == 1:
                                region_perimiter += 1
                                local_fences = update_perimiter(fences, next_x, next_y, dir, plants[y][x])
                            elif next_y < len(local_fences) and next_x < len(local_fences[0]) and local_fences[next_y][next_x] == 0:
                                next_plant = (abs(next_x+x_offsets[dir]), abs(next_y+y_offsets[dir]))
                                region_locations.add(next_plant)
                                found_locations.add(next_plant)
                #print(f"Region: {plants[y][x]}, perim: {region_perimiter}")
                #print_matrix(local_fences)
                total_price += get_score_updated(local_fences) * region_area
                #print()

    return total_price

def get_score_updated(fences):
    corners = 0
    for y in range(len(fences)):
        for x in range(len(fences)):
            #so instead of checking for the lines, we are going to instead look for corners, probably would have been easier to start with this 
            if fences[y][x] == 2:
                new_corners = 0
                if y+1 < len(fences) and 0 <= x-1 and fences[y+1][x-1] == 2:
                    new_corners += 1
                if y+1 < len(fences) and x+1 < len(fences[y]) and fences[y+1][x+1] == 2:
                    new_corners += 1
                if y+2 < len(fences) and new_corners == 2 and fences[y+2][x] == 2 and fences[y+1][x] == 0:
                    new_corners = 0
                corners += new_corners
        #print(f"{y}\t{corners}")
        #feels like cheating, probably because it is
    if corners < 4:
        corners = 4
    #print(corners)
    return corners
            




def reset_fences(fences):
    for y in range(len(fences)):
        for x in range(len(fences[y])):
            if fences[y][x] == 2:
                fences[y][x] = 1
    return fences

def update_perimiter(fences, x, y, dir, r):
    #go each direction
    x_offsets = [0, 2, 0, -2]
    y_offsets = [-2, 0, 2, 0]

    cur_x = x+x_offsets[dir]
    cur_y = y+y_offsets[dir]
    
    while 0 < cur_y < len(fences) and 0 < cur_x < len(fences[0]) and fences[cur_y][cur_x] == 1:
        #make sure we are not wandering off
        adjacent = False
        if 0 <= cur_x < len(fences[0]) and 0 <= cur_y < len(fences):
            if dir % 2 == 0:
                #travelling vertically
                test_y = cur_y - y_offsets[dir]//2 #trust me on this one (famous last words)
                if fences[test_y][cur_x+1] == r or fences[test_y][cur_x-1] == r:
                    adjacent = True
            else:
                test_x = cur_x - x_offsets[dir]//2
                if fences[cur_y+1][test_x] == r or fences[cur_y-1][test_x] == r:
                    adjacent = True
                #watch me get an out of bounds because of this
        if adjacent:
            fences[cur_y][cur_x] = 2
            cur_x += x_offsets[dir]
            cur_y += y_offsets[dir]
        else:
            break
    fences[y][x] = 2
    return fences



def solve_part_2():
    plants = get_lines()
    fences = get_fence_matrix(plants)
    #print_matrix(fences)
    total_price_2 = get_fencing_price_2(fences, plants)
    print(f"Total price for part 2: {total_price_2}")

solve_part_1()
solve_part_2()



"""
It has been over three hours since I finished the first half of this problem
the entire problem took the majority of my working day
and yet
I don't know if I've ever felt this good solving a coding puzzle

I know my solution isn't the fastest or prettiest or anything like that
but I'll be damned if it isn't mine
There were so many points where I could tell I was making progress but couldn't tell how far away I was
I just kept saying "I'll only need like 30 more minutes"
eventually I was right


regardless, I never want to look at this problem again


"""