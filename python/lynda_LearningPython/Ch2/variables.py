#
#Example file for python variables
#

# Declare a variable and initialise it
f = 0
print f

# re-declare the variable
f = "abc"
print f

# Different types cannot be combined
# Below fails
# print "string type " + 123
# works
print "string type " + str(123)

# Test of global vs. local variables
def someFunction():
    #global f
    f = "def"
    print f

def someFunction2():
    global f
    f = "def"
    print f


#Global f stays the same    
someFunction()
print f

#global f now acted on in function
someFunction2()
print f

#delete a variable
del f
print f
