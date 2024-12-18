#new file reading setup
filepath = "day2/day2-input.txt"
file = open(filepath, "r")

#I remember doing a somewhat similar leetcode problem before 
safe_level_count = 0

#general approach, assume level is safe, and check to see if contradiction is true
#proof by "nuh uh"
#i swear that joke is way better when you're surrounded by math majors

def check_line(levels) -> int: #returns 1 if safe, 0 if unsafe
    ascending = True
    descending = True

    for i in range(len(levels)-1):
        level_a = int(levels[i])
        level_b = int(levels[i+1])
        difference = level_a - level_b
        if abs(difference) == 0 or abs(difference) > 3:
            return 0
        if level_a > level_b:
            ascending = False
        elif level_a < level_b:
            descending = False
        if ascending == False and descending == False:
            return 0
    return 1

for line in file:
    levels = line.split(" ")
    safe_level_count += check_line(levels)

print(safe_level_count)

#correct answer: 631

"""
In what I expect to be a recurring theme for this, the second puzzle is very similar to the first
so I'll just keep doing them in the same file
I'm sure this could be done a little faster than brute force o(n^2) but I will be taking that approach
"""
#repoen the file at the beginning
file.close()
file = open(filepath, "r")
safe_level_count_2 = 0

for line in file:
    levels = line.split(" ")
    for i in range(len(levels)):
        new_list = levels.copy()
        new_list.pop(i)
        if check_line(new_list) == 1:
            safe_level_count_2 += 1
            break


print(safe_level_count_2)


#took some toying around but finally got the answer of 665






