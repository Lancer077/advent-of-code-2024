from collections import defaultdict, deque

filepath = "day5/day5-input.txt"
file = open(filepath, "r")

"""
1. grab the list of rules
2. grab the line holding the update
3. assume the line is valid, loop through each entry trying to prove false
"""
page_rule_list_a = []
page_rule_list_b = []
for line in file:
    if "|" in line:
        line = line.replace("\n", "")
        nums = line.split("|")
        page_rule_list_a.append(nums[0])
        page_rule_list_b.append(nums[1])
    else:
        break


#now that we have the rules read into the tuple rule list, we can loop through and check the validity of the updates

def get_instance_locations(page_num, rule_list):
    locations = []
    for i in range(len(rule_list)):
        if rule_list[i] == page_num:
            locations.append(i)
    return locations


def check_page_validity(page_loc, page_list) -> bool:
    page_num = page_list[page_loc]
    #get every instance of page_num in page_rule_list_a
    a_locations = get_instance_locations(page_num, page_rule_list_a)
    b_locations = get_instance_locations(page_num, page_rule_list_b)
    
    for i in range(len(a_locations)):
        b_page_num = page_rule_list_b[a_locations[i]]

        if b_page_num in page_list:
            b_page_loc = page_list.index(b_page_num)
            if b_page_loc < page_loc:
                return False
    for i in range(len(b_locations)):
        a_page_num = page_rule_list_a[b_locations[i]]
        if a_page_num in page_list:
            a_page_loc = page_list.index(a_page_num)
            if a_page_loc > page_loc:
                return False
    return True

update_total = 0

for line in file:
    valid = True
    pages = line.split(",")
    for i in range(len(pages)):
        if check_page_validity(i, pages) == False:
            valid = False
    if valid:
        median_loc = int(len(pages)/2)
        median = pages[median_loc]
        update_total += int(median)

print(f"Total: {update_total}")


"""
So this doesn't get me the correct answer for the example dataset, but works for the real dataset
not complaining 
now focusing on part b
I needed to get external help to understand topological sort, but still figured I could get some good practice with it
"""
file.close()
file = open(filepath, "r")

rules = []
for line in file:
    if "|" in line:
        line = line.replace("\n", "")
        x, y = map(int, line.split("|"))
        rules.append((x,y))
    else:
        break
updates = []
for line in file:
    updates.append(list(map(int, line.split(','))))


def build_graph(rules, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    relevant_pages = set(update)
    for x, y in rules:
        if x in relevant_pages and y in relevant_pages:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree.setdefault(x,0)
    return graph, in_degree

def topo_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all pages are included, return the sorted list; otherwise, it's invalid
    if len(sorted_pages) == len(in_degree):
        return sorted_pages
    return None  # Invalid case if a cycle is detected

def check_and_reorder_update(update, rules):
    """Checks if an update is ordered correctly; if not, reorders it."""
    graph, in_degree = build_graph(rules, update)
    sorted_pages = topo_sort(graph, in_degree)
    if sorted_pages:
        # Check if the update matches the sorted pages
        if update == sorted_pages:
            return update, True  # Already in correct order
        return sorted_pages, False  # Corrected order
    return update, False


reorder_middle_sum = 0
for update in updates:
    reordered_update, is_correct = check_and_reorder_update(update, rules)
    if not is_correct:
        middle_index = len(reordered_update)//2
        reorder_middle_sum += reordered_update[middle_index]

print(reorder_middle_sum)







