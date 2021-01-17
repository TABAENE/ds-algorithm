# Amazon: Find unique number in an array.

aa = [1,3,5,5,7,10,10,6,6]

frequency = {}

for a in aa:
    if a in frequency:
        frequency[a] = frequency[a] + 1
    else:
        frequency[a] = 1

print (frequency)
print ("Unique element.", [k for k, v in frequency.items() if v ==1])

"""
Output:
{1: 1, 3: 1, 5: 2, 7: 1, 10: 2, 6: 2}
Unique element. [1, 3, 7]
"""
