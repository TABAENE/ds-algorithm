## Find the longest sequence of 1’s with one flip.

input = [1,1,0,1,1,0,1,0,1,1]

# Expected output: 4

def get_new_input(input):
    ones_total = 0
    new_input = []
    # Below loop complexity would be n.
    for i in input:
        if i == 1:
            ones_total += 1
        else:
            new_input.append(ones_total)
            new_input.append(i)
            ones_total = 0
    new_input.append(ones_total)
    return new_input


def get_sum_of_ones_longest_sequence_with_one_flip(input):
    if len(input) == 1:
        return
    new_input = get_new_input(input)
    print ("New input \n", new_input)
    # [2, 0, 2, 0, 1, 0, 2]
    if new_input:
        # As we are using step 2, so below loop complexity would be n/2.
        new_input = new_input[::2]
    max_sum = 0
    for i in range(len(new_input) - 1):
        if (i + 1) <= len(new_input) - 1:
            new_sum = new_input[i] + new_input[i + 1]
            if new_sum > max_sum:
                max_sum = new_input[i] + new_input[i+1]
    print ("Sum:", max_sum)

# Total complexity - n + n/2 => n
get_sum_of_ones_longest_sequence_with_one_flip(input)
