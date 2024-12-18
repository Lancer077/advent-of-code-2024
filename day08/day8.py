

filepath = "day08/input.txt"
file = open(filepath, "r")

#read in file
frequency_graph = []
antinode_graph = []
replace_regex = r"[a-z]|[A-Z]|\d"
for line in file:
    line = line.replace("\n", "")
    frequency_line = []
    antinode_line = []
    for i in range(len(line)):
        frequency_line.append(line[i])
        antinode_line.append(".")
    frequency_graph.append(frequency_line)
    antinode_graph.append(antinode_line)

antinode_graph_2 = antinode_graph.copy()

def is_in_range(graph, x, y):
    if y < 0:
        return False
    if x < 0:
        return False
    if y > len(graph)-1:
        return False
    if x > len(graph[y])-1:
        return False
    return True

#build the antinode graph
for y_orig in range(len(frequency_graph)):  #putting the BIG in Big O notation
    for x_orig in range(len(frequency_graph[y_orig])):
        if frequency_graph[y_orig][x_orig] != ".":
            antenna = frequency_graph[y_orig][x_orig]
            for y_next in range(len(frequency_graph)):
                for x_next in range(len(frequency_graph[y_next])):
                    if x_orig != x_next and y_orig != y_next and antenna == frequency_graph[y_next][x_next]:
                        x_diff = abs(x_orig - x_next)
                        y_diff = abs(y_orig - y_next)
                        if x_orig > x_next:
                            antinode_a_x = x_orig + x_diff
                            antinode_b_x = x_next - x_diff
                        else:
                            antinode_a_x = x_orig - x_diff
                            antinode_b_x = x_next + x_diff
                        if y_orig > y_next:
                            antinode_a_y = y_orig + y_diff
                            antinode_b_y = y_next - y_diff
                        else:
                            antinode_a_y = y_orig - y_diff
                            antinode_b_y = y_next + y_diff
                        if is_in_range(antinode_graph, antinode_a_x, antinode_a_y):
                            antinode_graph[antinode_a_y][antinode_a_x] = "#"
                        if is_in_range(antinode_graph, antinode_b_x, antinode_b_y):
                            antinode_graph[antinode_b_y][antinode_b_x] = "#"


antinode_count = 0
for y in range(len(antinode_graph)):
    for x in range(len(antinode_graph[y])):
        if antinode_graph[y][x] == "#":
            antinode_count += 1

print(f"Antinode count for part 1: {antinode_count}")


"""
YESSS LETS GOOO

Alright round 2
Looks simple enough, can reuse the in_bounds and just throw a while loop around it
"""


#so now we always count the locations of the antennas, neat

for y_orig in range(len(frequency_graph)):
    for x_orig in range(len(frequency_graph[x_orig])):
        if frequency_graph[y_orig][x_orig] != ".":
            antenna = frequency_graph[y_orig][x_orig]
            for y_next in range(len(frequency_graph)):
                for x_next in range(len(frequency_graph[y_next])):
                    if y_orig != y_next and x_orig != x_next and antenna == frequency_graph[y_next][x_next]:
                        antinode_graph_2[y_orig][x_orig] = "#"
                        antinode_graph_2[y_next][x_next] = "#"
                        #now we go in a line, both directions
                        x_diff = abs(x_orig - x_next)
                        y_diff = abs(y_orig - y_next)
                        #"you can't just copy code" <- 🤓
                        if x_orig > x_next:
                            line_a_x = x_orig
                            line_a_x_offset =  x_diff
                            line_b_x = x_next 
                            line_b_x_offset = - x_diff
                        else:
                            line_a_x = x_orig 
                            line_a_x_offset = - x_diff
                            line_b_x = x_next 
                            line_b_x_offset = x_diff
                        if y_orig > y_next:
                            line_a_y = y_orig 
                            line_a_y_offset = y_diff
                            line_b_y = y_next 
                            line_b_y_offset = - y_diff
                        else:
                            line_a_y = y_orig 
                            line_a_y_offset = - y_diff
                            line_b_y = y_next 
                            line_b_y_offset = y_diff
                        line_a_x += line_a_x_offset
                        line_b_x += line_b_x_offset
                        line_a_y += line_a_y_offset
                        line_b_y += line_b_y_offset
                        while is_in_range(antinode_graph_2, line_a_x, line_a_y):
                            antinode_graph_2[line_a_y][line_a_x] = "#"
                            line_a_x += line_a_x_offset
                            line_a_y += line_a_y_offset
                        while is_in_range(antinode_graph_2, line_b_x, line_b_y):
                            antinode_graph_2[line_b_y][line_b_x] = "#"
                            line_b_x += line_b_x_offset
                            line_b_y += line_b_y_offset
                        


antinode_count_2 = 0
for y in range(len(antinode_graph_2)):
    for x in range(len(antinode_graph_2[y])):
        if antinode_graph_2[y][x] == "#":
            antinode_count_2 += 1

print(f"Antinode count for part 2: {antinode_count_2}")





"""
This is without a doubt the worst code to ever get the answer
but it did get the answer

"""

