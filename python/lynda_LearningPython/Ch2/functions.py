#
#Example working with functions
#

# define a function
def func1():
    print "I am a function"


func1()
#prints None as there is no return
print func1()
#print address as functions are objects of type function
print func1

#function with arguments
def func2(arg1, arg2):
    print arg1, " ", arg2

func2(10,20)
print func2(10,20)

# functions can return a value
def cube(x):
    return x*x*x

print cube(3)

#default values
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#2**1
print power(2)
#2**3
print power(2,3)
#2**3 as python can work out var names if included on calling
print power(x=4,num=2)

#showing use of *
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print multi_add(4,5,10,4)

print multi_add()
