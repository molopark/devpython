print("""
this
is
text""")

a = "Hello world"
print(a)
#length
print(len(a))
#index
print(a[4])
print(a[3:5])
print((a+'\n')*2)

#variable
name = 'apple'
print('to '+name+' Lorem ipsum dolor sit amet, '+name+' consectetur adipisicing elit, sed do eiusmod tempor '+name+' incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

#positional formatting
print('to {} Lorem ipsum dolor sit amet, {} consectetur adipisicing elit, sed do eiusmod tempor {} incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.format('apple', 12, 'apple'))

#named placeholder
print('to {name} Lorem ipsum dolor sit amet, {age:d} consectetur adipisicing elit, sed do eiusmod tempor {name} incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.format(name='apple', age=12))
