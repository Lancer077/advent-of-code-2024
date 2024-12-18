

filepath = "day07/input.txt"
file = open(filepath, "r")

#going to use a recursive approach because that seems like the most logical thing to do
def valid_equation(target, values):
    results = recursive_eval_expression_2(values, values[0], 1)
    if target in results:
        return True
    return False

def concat(val_a: int, val_b: int) -> int:
    b_str = str(val_b)
    val_c = val_a * ((10 ** len(b_str)))
    val_c += val_b
    return val_c

def recursive_eval_expression(values, cur_val, index):
    if index == len(values):
        return [cur_val]
    plus_results   = recursive_eval_expression(values, cur_val + values[index], index + 1)
    mult_results   = recursive_eval_expression(values, cur_val * values[index], index + 1)
    return plus_results + mult_results

def recursive_eval_expression_2(values, cur_val, index):
    if index == len(values):
        return [cur_val]
    plus_results   = recursive_eval_expression_2(values, cur_val + values[index], index + 1)
    mult_results   = recursive_eval_expression_2(values, cur_val * values[index], index + 1)
    concat_results = recursive_eval_expression_2(values, concat(cur_val, values[index]), index + 1)
    return plus_results + mult_results + concat_results


if True:
    total_result = 0
    for line in file:
        line = line.split(":")
        calculation_result = int(line[0])
        values = line[1].split(" ")
        values = values[1:] #need to drop the first one
        for i in range(len(values)):
            values[i] = int(values[i])
        if valid_equation(calculation_result, values):
            total_result += calculation_result

    print(f"Total Result for given part: {total_result}")

"""
I figured this one would be easier to just modify the code instead of rewriting everything
probably my favorite problem so far because it felt just difficult enough
"""




