# A way to create lists on one line of code

my_list = [((num*1),(num*2),(num*3)) for num in range(0,100)]

print(my_list)

# List comprehension can be combined with ternary operators

# this can be used to filter list

my_list2 = [num for num in range(0,100) if num < 10]

print(my_list2)

my_list3 = [num if num < 10 else 0 for num in range(0,100)]

print(my_list3)

inventory_names = ['Titanium plating', 'Adaptive Frame', 'Isolined Magnet', 'Adhesive', 'Circuit Board', 'Memory Chip']
inventory_numbers = [5, 12, 25, 10, 7, 16]
replenish_list = [(name, number) for name, number in zip(inventory_names, inventory_numbers) if number < 10]

print(replenish_list)

# Combine list comprehension

comb_comp = [[(x,y) for x in range(3)] for y in range(9)]
for row in comb_comp:
    print(row)

# Exercise
# Create the field for a chess board
# abcdefgh
# 12345678

chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
for row in chess_board:
    print(row)