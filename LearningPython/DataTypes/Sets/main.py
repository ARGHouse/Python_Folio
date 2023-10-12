my_set = {1,2,3,4,4,4} #duplicate values will be eliminated

#use methods
my_set.add(5)
my_set.remove(2)
print(len(my_set))
print(my_set)

#indexing and slicing does not work
#use type conversion
print(list(my_set)[0])
print(list(my_set)[1])
print(list(my_set)[2])
print(list(my_set)[3])

#comparison
set1 = {2,4,7,9,1,0}
set2 = {5,1,3,2,6,5}
print(set1.union(set2)) #joined set
print(set1.intersection(set2)) #shared set elements
print(set1.difference(set2)) #unique set elements

print(set1 | set2) #alt join
print(set1 & set2) #alt intersect
print(set1 - set2) #alt difference


