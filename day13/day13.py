

def get_file():
    filepath = "day13/input.txt"
    file = open(filepath, "r")
    return file

def clean_line(line: str):
    line = line.split(":")
    line = line[1]
    line = line.replace("X", "")
    line = line.replace("Y", "")
    line = line.replace("+", "")
    line = line.replace("=", "")
    line = line.split(",")
    x = int(line[0])
    y = int(line[1])
    return (x, y)


def read_file(file, part: int):
    cur_line_counter = 0
    button_list = []
    target_list = []
    for line in file:
        if cur_line_counter % 4 != 3: 
            cur_loc = clean_line(line)
            if cur_line_counter % 4 == 0 or cur_line_counter % 4 == 1:
                #grabbing button xy
                button_list.append(cur_loc)
            elif cur_line_counter % 4 == 2:
                if part == 2: #CODE EXTENDABILITY BABY
                    x = cur_loc[0] + 10000000000000
                    y = cur_loc[1] + 10000000000000
                    cur_loc = (x,y)
                target_list.append(cur_loc)
        cur_line_counter += 1
    file.close()
    return button_list, target_list


def loop_and_solve(button_list, target_list, part):
    total_cost = 0
    for i in range(len(target_list)):
        button_a = button_list[i*2]
        button_b = button_list[i*2+1]
        target = target_list[i]
        if part == 1:
            total_cost += find_token_count(button_a, button_b, target)
        elif part == 2:
            total_cost += find_token_count_2(button_a, button_b, target)
    return total_cost


def find_token_count(button_a, button_b, target):
    solutions = []
    for button_press_b in range(101): #rules state we can assume max of 100 button presses
        cur_total_x = 0
        cur_total_y = 0
        cur_total_x = button_b[0] * button_press_b
        cur_total_y = button_b[1] * button_press_b
        button_press_a = 0
        while cur_total_x <= target[0] and cur_total_y <= target[1] and button_press_a < 101:
            if cur_total_x == target[0] and cur_total_y == target[1]:
                cur_solution = (button_press_a, button_press_b)
                solutions.append(cur_solution)
            button_press_a += 1
            cur_total_x += button_a[0]
            cur_total_y += button_a[1]
    if len(solutions) == 0:
        return 0
    costs = []
    for solution in solutions:
        costs.append(calculate_cost(solution))
    return min(costs)


def calculate_cost(solution):
    a_cost = 3
    b_cost = 1
    cost = (solution[0] * a_cost) + (solution[1] * b_cost)
    return cost


def solve_part_1():
    part = 1
    file = get_file()
    button_list, target_list = read_file(file, part)
    total_cost = loop_and_solve(button_list, target_list, part)
    print(f"Total cost for part 1: {total_cost}")


"""
heyo not too shabby that one
Took maybe an hour max
let's get part 2

and of course we don't get any way to check our code for this part
still not gonna stop me (because I've got nothing better to do)

And naturally the computation hits an absolute brick wall at part 2, let it run for a couple minutes
and didn't even finish 3 of 320 puzzles

Then I went online and people were talking about how it's not a simulation problem but instead a math problem
Simulating it worked for the first part, but will take forever for the second part

------------

and it's just a system of equations question
better computing power just makes worse programmers
after looking around because numpy wanted to give me negative numbers and non integers,
discovered sympy and diophantine
"""

from z3 import Int, Solver, sat

"""
def find_token_count_2(button_a, button_b, target):
    x, y = Ints('x y')
    sol = str(solve(button_a[0] * x + button_b[0] * y == target[0], button_a[1] * x + button_b[1] * y == target[1], x > 0, y > 0))
    print(f"solution: {sol}")
    #print(type(sol))
"""


def find_token_count_2(button_a, button_b, target):
    x = Int('x')
    y = Int('y')

    solver = Solver()
    #for some reason, the solver would always return unsat unless I was adding the two equations
    solver.add(button_a[0] * x + (button_b[0] * y) == target[0], button_a[1] * x + (button_b[1] * y) == target[1])
    solver.add(x >= 0)
    solver.add(y >= 0)
    
    result = solver.check()
    if result == sat:
        model = solver.model()
        x_loc = int(str(model[x])) #now I know this looks bad
        y_loc = int(str(model[y])) #I agree
        solution = (x_loc, y_loc)
        return calculate_cost(solution)
    return 0

    

def solve_part_2():
    part = 2
    file = get_file()
    button_list, target_list = read_file(file, part)
    total_cost = loop_and_solve(button_list, target_list, part)
    print(f"Total cost for part 2: {total_cost}")




solve_part_1()
solve_part_2()

"""
Always feels good when your solution for part 2 is faster or just as fast as part 1
Pride is definitely a little hurt but without that I would have never learned about z3 and how 
incredibly useful it is.


AND WE ARE OVER HALF WAY THERE MAKE SOME NOISE EVERYBODY!!!!!!

"""
