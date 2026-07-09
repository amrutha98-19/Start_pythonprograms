# Set operations
#union ->Combines all unique elements from both sets.
#intersection -> Returns the common elements present in both sets
#difference ->Returns elements present in the first set but not in the second set.
#symmetric Difference -> Returns elements that are present in either set but not in both sets.

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1.union(set2)) #
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))