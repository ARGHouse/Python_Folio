test = 'i am shouting'
print(test.upper())

test2 = 'I AM WHISPERING'
print(test2.lower())

fd_usrname = 'AGenT SMitHFOOK'
print(fd_usrname)
print(dir(fd_usrname))
print(fd_usrname.isalpha())
unfck_usrname = fd_usrname.strip('FOOK').title()
print(unfck_usrname)
print(dir(unfck_usrname))
print(unfck_usrname.isalpha())
spcls_usrname = 'NonameSpacelessMan'
print(spcls_usrname)
print(spcls_usrname.isalpha())
num_usrname = "12345"
print(num_usrname)
print(num_usrname.isalnum())


ex_str = 'Python is my favourite game programming language'

print(ex_str)

print(ex_str.replace("Python", "GDScript"))
