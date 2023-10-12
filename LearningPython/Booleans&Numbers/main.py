#booleans and numbers
print(1 == 10) #true if is equal
print(1 != 10) #true if is different
print(10 > 10) #true if greater than ten
print(not 10 > 10)

#booleans and lists and strings
print(1 in (1,2,3))
print('e' in 'hello')
print(4 not in [1,2,3])

#booleans by themselves
print(True)
print(not True)

#data conversion
#check if the key 1 exists in the dict
#check if the value 'four' exists
e_dict = {1:'one', 2: 'two', 3:'three'}
#a
print( 1 in e_dict )

#b
print( 'four' in e_dict.values())
print( 'three' in e_dict.values())

#bool
#truthy - all values that will be converted to true
#falsy - all values that will be converted to false

#falsy values
#0 or 0.0 (int or float)
#"(empty string)
#[],(),{}(empty list, tuple, set, dict)
#None (absense of a value)

#bool function
print(bool(123123123))
print(bool(0.0000000))
print(bool(0.0000001))
print(bool(None))