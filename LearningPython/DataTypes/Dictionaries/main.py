#basics
test_dict = {'A':123, 'B':[1,2,3], 1: True} #Cannot duplicate keys
print(test_dict.items())
print(test_dict.values())
print(test_dict.keys())
print(len(test_dict))

#converting a dictionary
print(list(test_dict))
print(tuple(test_dict))
print(str(test_dict))

#indexing with dictionaries
print(test_dict['A']) #If input a key that does not exist = error
print(test_dict.get('A')) #<<< better, if input a key that not exist, no return, no crash or error

#exercise
test_dict.update({'Another Key': (1,2,3)})
test_dict.update(C = 'test', D = '456')
test_dict['E'] = 100
print(test_dict)