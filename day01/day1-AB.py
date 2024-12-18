#get the file and set up the file reading
filepath = "day01/day1-input.txt"
file = open(filepath, "r")

#originally thought about sorting the list as I read it in, but I got a late start to advent of code
#so I'll just use python's list.sort

#start with making two empty lists
historian_list_a = []
historian_list_b = []

#now we will create a function that takes in a list and a number to add to the list


for line in file:
    new_id_list = line.split("   ")
    id_a = int(new_id_list[0])
    id_b = int(new_id_list[1])
    historian_list_a.append(id_a)
    historian_list_b.append(id_b)

#using python sort
historian_list_a.sort()
historian_list_b.sort()

#print(*historian_list_a)

#now that the files have been read in and sorted
#we need to iterate through each entry, and find the differences, then add them to the total difference
total_difference = 0
print(len(historian_list_a))
print(len(historian_list_b))
for i in range(len(historian_list_a)):
    entry_a = historian_list_a[i]
    entry_b = historian_list_b[i]
    current_difference = abs(entry_a - entry_b)
    total_difference += current_difference
print(total_difference)

#got the correct answer

"""
PART B:
since the problem is so similar, and benefits from an already already sorted list, I decided to just do it in the same file
So the plan is to get a number from historian_list_a, loop through historian_list_b, find all entries that match, and calculate a score based on that
seems easy enough
"""

total_similarity_score = 0
for id_a in historian_list_a:
    appearance_count = 0
    for id_b in historian_list_b:
        if id_a == id_b:
            appearance_count += 1
        elif id_a < id_b:
            break #since the lists are already sorted, we can save on runtime
    current_similarity_score = appearance_count * id_a #we apply the similarity score calculation
    total_similarity_score += current_similarity_score #and add it to the total

print(total_similarity_score)

#correct again!