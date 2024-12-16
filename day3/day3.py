#using regex
import re

#read the file in
filepath = "day3/day3-input.txt"
file = open(filepath, "r")

#regex time
#I know a lot of people online complain about it but it's really not that hard
#and it's a crazy powerful tool

#we want to get all of the times where we have a string matching the pattern "mul(x, y)"
#where x and y are integers with 1-3 digits. I played around a bit in regex101.com and came up with the following
#  "mul\(\d{1,3},\d{1,3}\)"  lets see if it works

def get_mul_total(line: str) -> int:
    nums_matches = re.findall(find_nums_pattern, line)
    return (int(nums_matches[0]) * int(nums_matches[1]))
    

find_mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
find_nums_pattern = r"\d{1,3}"
mul_total_1 = 0
for line in file:
    mul_matches = re.findall(find_mul_pattern, line)
    for match in mul_matches:
        mul_total_1 += get_mul_total(match)
print(mul_total_1)
#got the answer: 184511516

"""
Alright now we push forward to work on part 2 and it looks like regex is probably the right idea for this one as well
Since the program can be in a state of enabled or !enabled, it looks like a boolean would work for that
lets do it
"""
#reopen the file because seek is for nerds
file.close()
file = open(filepath, "r")

enabled = True  #instructions say to assume program starts in 'enabled' state
#I'm guessing making the instructions line by line just would have been too easy
#Can't just do the same thing to the whole line unfortunately
#what I can do is strip the line of all patterns that do not match a given pattern
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
strip_pattern = r"(do\(\))|(don\'t\(\))|(mul\(\d{1,3},\d{1,3}\))" #this will only match with the stuff we care about

mul_total_2 = 0
for line in file:
    str_matches = re.findall(strip_pattern, line)
    for str_match in str_matches:
        if str_match[0] != '':
            enabled = True
        elif str_match[1] != '':
            enabled = False
        elif str_match[2] != '':
            if enabled:
                mul_total_2 += get_mul_total(str_match[2])
print(mul_total_2)

    
"""
and that works, 90044227
that's a wrap on day 3, pretty fun challenge, haven't used regex in about a year so it was some good practice

"""



























