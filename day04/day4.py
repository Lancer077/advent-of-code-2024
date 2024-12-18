filepath = "day04/day4-input.txt"
file = open(filepath, "r")

"""
This one looks, not fun but hopefully relatively straightforward
Words may be:
- Horizontal
- Vertical
- Diagonal
- Backwards
- Overlapping other words
given this, I am just going to loop through the lines, each time I find the letter X, I will 
look each direction for the rest of the word and return accordingly
"""

lines = []

#read the whole file into memory because we will need previous/future lines anyways
#also has an added benefit of allowing us to reuse the reading in part B
for line in file:
    lines.append(line)



def check_direction(column, line, column_offset, line_offset) -> int:
    match_str = "MAS" #we have already matched the x, no need to include it here
    for i in range(len(match_str)):
        match_letter = match_str[i]
        line += line_offset
        column += column_offset
        if line == 140:
            return 0
        elif lines[line][column] != match_letter:
            return 0
    return 1

def check_all_directions(line, column) -> int:
    cur_xmas_counter = 0
    #create two lists to help check all directions and prevent code reuse
    #for those interested, this is the order:
    #check horizontal forward (1, 0)
    #check horizontal backward (aka reverse) (-1, 0)
    #check vertical down (0, 1)
    #check vertical up (0, -1)
    #check diagonal right/forward and down (1, 1)
    #check diagonal left/reverse and down (-1, 1)
    #check diagonal left/reverse and up (-1, -1)
    #check diagonal right/forward and up (1, -1)
    x_offset_list = []  #start with empty offset lists and build them up
    y_offset_list = []  #easier to maintain, looks nicer, and makes it easier to prevent out of bounds
    #if we can go up
    if line > 2: 
        x_offset_list.append(0)
        y_offset_list.append(-1)
    #check if we can go down
    if line < len(lines)-3: #checks if we can go downwards, 
        x_offset_list.append(0)
        y_offset_list.append(1)
    #check if we can go left
    if column > 2:
        x_offset_list.append(-1)
        y_offset_list.append(0)
    #check if we can go right
    if column < len(lines[0])-2: #assumes that all lines have equal length
        x_offset_list.append(1)
        y_offset_list.append(0)
    
    #now we check the diagonals
    if line > 2 and column > 2:
        x_offset_list.append(-1)
        y_offset_list.append(-1)
    if line > 2 and column < len(lines[0])-2:
        x_offset_list.append(1)
        y_offset_list.append(-1)
    if line < len(lines)-3 and column > 2:
        x_offset_list.append(-1)
        y_offset_list.append(1)
    if line < len(lines)-3 and column < len(lines[0])-2:
        x_offset_list.append(1)
        y_offset_list.append(1)

    for i in range(len(x_offset_list)):
        cur_xmas_counter += check_direction(column, line, x_offset_list[i], y_offset_list[i])
    return cur_xmas_counter


xmas_counter = 0
for line in range(len(lines)):
    for column in range(len(lines[line])):
        if lines[line][column] == "X":
            xmas_counter += check_all_directions(line, column)

print(xmas_counter)


#woah that was a lot of code, want to see even more?



"""
alrighty, time for part 2
wait why does this seem easier
we gotta find each instance of the letter A
then we gotta check if it has two SAM going diagonally
seems simple enough (hopefully it stays that way)

We can also skip worrying about out of bounds edge cases because of the simplicity
"""

def check_x_exists(x_pos:int, y_pos:int) -> int:
    right_up   = lines[y_pos+1][x_pos-1]
    right_down = lines[y_pos+1][x_pos+1]
    left_up    = lines[y_pos-1][x_pos-1]
    left_down  = lines[y_pos-1][x_pos+1]
    return_val = 0.0
    if right_up == "S" and left_down == "M":
        return_val += 0.6
    if right_up == "M" and left_down == "S":
        return_val += 0.6
    if left_up == "S" and right_down == "M":
        return_val += 0.6
    if left_up == "M" and right_down == "S":
        return_val += 0.6
    return int(return_val) #if only one half of the equation is right, the cast to int fixes this
    #I'm kinda proud of this idea


xmas_counter_2 = 0
for y in range(len(lines)-2):
    for x in range(len(lines[0])-2):
        if lines[y+1][x+1] == "A": #add 1 here to cut off the ends, same reason we subtract by 2 above
            xmas_counter_2 += check_x_exists(x+1, y+1)
print("Part 2 counter:")
print(xmas_counter_2)


"""
Part B was far easier, this was definitely not my favorite puzzle so far, but it was still pretty good
"""






