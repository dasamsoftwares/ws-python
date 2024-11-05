##############################################
#################### List ####################
##############################################

# Declare list
print('\n--DECLARE--')

lst_x = ['a',1,3.4,'b','2']
print(lst_x)

# Print elements in list
print('\n--SELECT--')

print(lst_x[0:3])
print(len(lst_x))
print(lst_x[0:len(lst_x)])
print(lst_x[0:len(lst_x):1])
print(lst_x[0:len(lst_x):2])
print(lst_x[-1])
print(lst_x[-2])
print(lst_x[-1:-2])
print(lst_x[-2:-1])
print(lst_x[-4:-1])

print(lst_x[-1:2])
# Insert/Update element in list
print('\n--INSERT/UPDATE--')
lst_x.append('new')             #Append adds element in end of list
print(lst_x)
lst_x.insert(3,'three')         #Insert element at particular location in list
print(lst_x)
lst_x[2]=100                    #Update element in list
print(lst_x)
lst_x[1:3] = [300, 400]
print(lst_x)

#Delete element from list
print('\n--DELETE--')
lst_x.pop()                     #Removes last element from list
print(lst_x)
print(lst_x.pop())              # Removes/Returns last element that is removed
lst_x.pop(1)                    # Remove element at particular index
print(lst_x)
del lst_x[3]                    # Remove element at particular index
print(lst_x)
del lst_x[0:1]                  # Remove elements in range
print(lst_x)
lst_x.remove(400)               # Remove first occurence of a particular value
print(lst_x)

#Operations
print('\n--OPERATIONS--')
lst_y = ['a','b','c']
print(lst_x+lst_y)              # Concatenate two lists
print(lst_y*3)                  # Repitition of three lists
print('a' in lst_y)             # Check if list contains element or not
print('z' in lst_y)


#Functions
print('\n--FUNCTIONS--')

print(len(lst_x))               # Find length of list
lst_x.append(400)               
print(lst_x.count(400))         # Counts the number of times the particular value is present in list
print(lst_x)
print(lst_y)
#print(cmp('a','a'))
print(lst_x.index(400))         # Print index of particular element in list.
lst_x.reverse()
print(lst_x)
lst_x.extend(lst_y)             # Appends list with Sequence(List, String, Tuple)
print(lst_x)
lst_x.extend('500')
print(lst_x)
tuple_x = (1,2,3)
lst_x.extend(tuple_x)   
print(lst_x)                    # Converts tuple to list using list() function
print(type(tuple_x))
print(type(list(tuple_x)))
lst_x=[1,5,0,3]                 # Sort a list
print(lst_x)
lst_x.sort()
print(lst_x)
