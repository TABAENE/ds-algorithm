# Amazon: Recursive staircase problem.

# Input: n = 4
# Output: 5
# (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)

# Input: n = 3
# Output: 3
# (1, 1, 1), (1, 2), (1, 2)


def count_ways(step_count):
    if step_count == 0:
        return 0
    if step_count == 1:
        return 1
    if step_count == 2:
        return 2
    # Bottom approach with below base case.
    d = {1: 1, 2: 2}
    for i in range(3, step_count + 1):
        # value 1 step before + value 2 step before.
        temp = d[i - 1] + d[i - 2]
        d[i] = temp
    return d[step_count]


print(count_ways(3))
