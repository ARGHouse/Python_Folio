
#all and statements are combined
#enitre and block is false if there is even one false
if True and True and False or True:
    print('True')

# Exercise
money_available = 100
hungry = True
bored = True
# Check if money_available > 80 and if hungry is true or if bored

#Checks and statement first > followed by or
if money_available > 80 and hungry == True or bored == True:
    print('eat something fancy!')

#nested if statements
x = '1'
if x in ['a','b','1']:
    print('a is in the list')
    if x.isalpha():
        print('it is a letter')

    #indepedent block
    if True:
        print('something')

#exercise
money_available = 100
hungry = False
bored = True

if money_available > 80:
    print('I have enough money!')
    if hungry:
        print('and I am hungry!')
        if bored:
            print('Eat something fancy :)')