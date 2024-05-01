# Given two sets, write a function, `left_diff`, that returns the "left"
# difference of the two sets, where the left difference refers to all elements
# that are in the first set, but not in the second set.

# Write your code here.
def left_diff(set1, set2):
    return set1 - set2 #difference
    # return set1 | set2 both sets without duplicates
    # return set1 & set2 shows pairs
    # return set1 ^ set2 shows unique only


set1 = { 1, 2, 5, 10 }
set2 = { 2, 6, 10, 12 }

print(left_diff(set1, set2))    # { 1, 5 }