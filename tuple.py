##############################################
#################### Tuple ####################
##############################################

# Declare tuple
print('\n--DECLARE--')
tuple_x = ('a',1,3.4,'b','2')

print(tuple_x)


# Print elements in tuple
print('\n--SELECT--')
print(tuple_x[0:3])
print(len(tuple_x))
print(tuple_x[0:len(tuple_x)])
print(tuple_x[0:len(tuple_x):1])
print(tuple_x[0:len(tuple_x):2])
print(tuple_x[-1])
print(tuple_x[-2])
print(tuple_x[-1:-2])
print(tuple_x[-2:-1])
print(tuple_x[-4:-1])
print(tuple_x[-1:2])


# Insert/Update element in tuple
# Tuple is Read only so Insert/Update is not allowed.

#Delete element from tuple
# Tuple is Read only so Insert/Update is not allowed.

#Operations
print('\n--OPERATIONS--')

tuple_y = ('a','b','c')
print(tuple_x+tuple_y)              # Concatenate two lists
tuple_z= tuple_y+tuple_x
print(tuple_z)
print(tuple_y*3)                  # Repetition of three lists
print('a' in tuple_y)             # Check if tuple contains element or not
print('z' in tuple_y)


#Functions
print('\n--FUNCTIONS--')

print(len(tuple_x))               # Find length of tuple
print(tuple_x.index(3.4))         # Print index of particular element in tuple.
