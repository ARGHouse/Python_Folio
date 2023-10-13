
inventory_names = ['Titanium plating', 'Adaptive Frame', 'Isolined Magnet', 'Adhesive', 'Circuit Board', 'Memory Chip']
inventory_numbers = [5, 12, 25, 10, 7, 16]

for name, number in zip(inventory_names, inventory_numbers):
    print(f'{name} amount: {number}')

# enumerate function -- get the current index

print(list(enumerate(inventory_names)))

for index, name in enumerate(inventory_names):
    print(f'{index}: {name}')
    if index == len(inventory_names) // 2: # I only want half
        print('halfway done!')

# Exercise
# Combine zip and enumerate to get 'Titanium plating [id: 0] - inventory: 5'
    print(' ')

for idx, inv_tuple in enumerate(zip(inventory_names, inventory_numbers)):
    print(f'{inv_tuple[0]} [id: {idx}] - inventory: {inv_tuple[1]}')