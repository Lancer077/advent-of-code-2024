



#this one looks a bit brutal but we will see
#thankfully we only need to read in one line!

def get_line() -> list:
    filepath = "day09/input.txt"
    file = open(filepath, "r")
    for line in file:
        disk = list(line[:-1])
        return disk

def create_disk(line_str):
    is_file = True
    file_id_counter = 0
    disk = []
    for i in range(len(line_str)):
        if not is_file:
            file_id_counter += 1
        disk = add_to_disk(disk, is_file, file_id_counter, line_str[i])
        is_file = not is_file
    return disk

def add_to_disk(disk, is_file, file_id, block):
    for i in range(int(block)):
        if is_file:
            disk.append(str(file_id))
        else:
            disk.append(".")
    return disk

def reorder_disk(disk):
    start_index = 0
    for i in range(len(disk)):
        disk, start_index = move_block(disk, len(disk)-i, start_index)
    return disk

def move_block(disk, index: int, start_index: int):
    index -= 1
    for i in range(len(disk)):
        if i+start_index >= index: #if we do not return before we reach the index
            return disk, i+start_index #then there are no more free spaces to the left
        if disk[i+start_index] == ".":
            #swap
            disk[i+start_index] = disk[index]
            disk[index] = "."
            return disk, i+start_index

def reorder_disk_2(disk):
    prev = ""
    for i in range(len(disk)):
        if i % 2700 == 0:
            print(i//2700)
        block_size = 1
        cur_index = len(disk)-i-1
        if disk[cur_index] != "." and disk[cur_index] != prev:
            prev = disk[cur_index]
            while disk[cur_index] == disk[cur_index - block_size]:
                block_size += 1
            disk = move_block_2(disk, cur_index, block_size)
        else: 
            block_size = 1
    return disk


def move_block_2(disk, index, block_size):
    #search for required open space
    for i in range(len(disk)):
        if i >= index:
            return disk
        valid_space = True
        for j in range(block_size):
            if disk[i+j] != ".":
                valid_space = False
        if valid_space:
            for j in range(block_size):
                disk[i+j] = disk[index-j]
                disk[index-j] = "."
            return disk
    return disk

def get_checksum(disk) -> int:
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            new_sum = int(disk[i]) * i
            if checksum > new_sum + checksum:
                print("OVERFLOW")
            checksum += (int(disk[i]) * i)
    return checksum



line_list = get_line()

disk = create_disk(line_list)

print(f"Disk Created")
disk = reorder_disk(disk)
print(f"Disk reordered")

checksum = get_checksum(disk)
print(f"Final Checksum for part 1: {checksum}")

"""
Ok that took significantly longer than it should have for reasons that will haunt me at night
let's just get on with part 2

Well this just goet way more interesting than previously
I think we can reuse a lot of the logic as before
"""

disk_2 = create_disk(line_list)
disk_2 = reorder_disk_2(disk_2)
checksum_2 = get_checksum(disk_2)
print(f"Final Checksum for part 2: {checksum_2}")





"""
Well the solution took pretty long but I'm overall happy with just completing it
"""



