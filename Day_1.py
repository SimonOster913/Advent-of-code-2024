# Challenge 1
# 1. find smallest value in lists - sort them
# 2. substract them
# 3. add the distances up

list_left = []
list_right = []

with open("Day_1_input.txt") as f:
    for line in f:
        out = line.strip().split()  # strip removes leading and trailing whitespaces or other inputs, split returns a list of all entries
        list_left.append(int(out[0]))
        list_right.append(int(out[1]))

list_left.sort(), list_right.sort()

result_part_1 = sum(
    abs(value_l - value_r) for value_l, value_r in zip(list_left, list_right)
)

print(result_part_1)

# Challenge 2
# 1. mulitply each number with its appearance in the right list
# 2. add up the sum

result_part_2 = 0
for value in list_left:
    appearances = [i for i, x in enumerate(list_right) if x == value]
    result_part_2 += value * len(appearances)

print(result_part_2)
