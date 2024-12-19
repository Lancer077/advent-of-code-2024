
def get_file():
    filepath = "day11/input.txt"
    file = open(filepath, "r")
    return file

def get_starting_arrangement(file):
    for line in file:
        line = line.replace("\n", "")
        return line.split(" ")

def get_digit_count(num: int) -> bool:
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def get_digit_split(num: int):
    size = get_digit_count(num)
    num1 = 0
    num2 = 0
    for i in range(size):
        if i < (size / 2):
            num1 += (num % 10) * (10 ** i)
        else:
            num2 += (num % 10) * (10 ** (i-(size/2)))
        num = num // 10
    return num1, num2

def blink(iterations: int, stone_list):
    #print(stone_list)
    updated_list = []
    for i in range(len(stone_list)):
        updated_list.append(int(stone_list[i]))
    stone_list = updated_list

    for iteration in range(iterations):
        #print(f"list len {len(stone_list)}")
        #print(f"Iteration: {iteration}")

        updated_list = []
        #apply rules to each stone
        for stone_index in range(len(stone_list)):
            stone = stone_list[stone_index]
            if stone == 0:
                #print(f"Option 1")
                updated_list.append(1)
            elif get_digit_count(stone) % 2 == 0:
                #print(f"Option 2")
                stone1, stone2 = get_digit_split(stone)
                updated_list.append(int(stone1))
                updated_list.append(int(stone2))
            else:
                #print(f"Option 3")
                stone *= 2024
                updated_list.append(stone)
            #print(stone)
            #print(f"list len {len(stone_list)}")
        stone_list = updated_list.copy()
        #print(stone_list)
    return stone_list



def count_stones(stone_list):
    return len(stone_list)


"""
I used to think the massive files were menacing but the fear of a massive file is nothing
compared to the fear of a small input file at least in this situation
stone rules:
if stone has number zero -> stone will have number 1
if stone number has even num of digits 
"""




file = get_file()
starting_arrangement = get_starting_arrangement(file)
final_arrangement_1 = blink(25, starting_arrangement)
stone_count_1 = count_stones(final_arrangement_1)
print(f"Final stone count for part 1: {stone_count_1}")

"""
Part 1 was surprisingly easy, had some minor mistakes in my code but nothing a little
debugging couldn't fix
and I just keep winning, all I need to do for part 2 is just change the iterations in the blink
"""

"""
final_arrangement_2 = blink(75, starting_arrangement)
stone_count_2 = count_stones(final_arrangement_2)
print(f"Final stone count for part 2: {stone_count_2}")
"""

"""
god damn it
So I think the problem lies within the fact that I need to keep copying and editing the array
which makes me think a linked list would be pretty good here

and I'm wrong again
"""
"""
from collections import deque

def list_to_deque(starting_arrangement):
    starting_deque = deque()
    for item in starting_arrangement:
        starting_deque.append(int(item))
    return starting_deque

def blink_deque(iterations: int, stone_deque: deque):
    for iteration in range(iterations):
        print(f"Iteration: {iteration}")

        updated_deque = deque()

        for stone_index in range(len(stone_deque)):
            cur_stone = stone_deque[stone_index]
            
            if cur_stone == 0:
                updated_deque.append(1)
            elif get_digit_count(cur_stone) % 2 == 0:
                stone1, stone2 = get_digit_split(cur_stone)
                updated_deque.append(stone1)
                updated_deque.append(stone2)
            else:
                updated_deque.append(cur_stone*2024)
        
        stone_deque = updated_deque
    return len(stone_deque)
starting_deque = list_to_deque(starting_arrangement)
stone_count = blink_deque(75, starting_deque)
print(f"Total stone count for part 2: {stone_count}")
"""

"""
Oh how naive I was
Eventually gave in because I couldn't figure out any way to speed up the calculations
significantly enough to make a real difference
So I'm now going off of Hyper Neutrino's solution on youtube
felt a little better because everyone online was talking about using a cache, which I've only covered conceptually in my data communications class
"""

from functools import cache

@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps-1)
    size = get_digit_count(stone)
    if size % 2 == 0:
        return count(int(str(stone)[:size//2]), steps-1) + count(int(str(stone)[size//2:]), steps-1)
    return count(stone * 2024, steps-1)

file_2 = get_file()

in_str: str

for line in file_2:
    line = line.replace("\n", "")
    in_str = line

stones = [int(x) for x in in_str.split()]
print(sum(count(stone, 75) for stone in stones))

"""
Of course the result that I found online found 75 iterations faster than my result found the 25
My pride is hurt a little bit
But I did get the chance to learn a lot about caching and I'll definitely be looking into it more
after I'm finished with advent of code

"""










