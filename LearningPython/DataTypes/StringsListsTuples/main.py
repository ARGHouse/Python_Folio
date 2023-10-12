test_str = 'this is a test'
test_lst = [1,2,3,4,'Tomato']

print(test_str.split())
print(list(test_str))
print(tuple(test_str))

print(' '.join(['one','two']))
print(type(str(test_lst)))
print(str(test_lst[0:4]).strip('[').strip(']').replace(',',' '))