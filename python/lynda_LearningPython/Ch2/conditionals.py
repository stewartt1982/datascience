#
# example file for working with conditionals
#

def main():
    x, y = 1000, 100

    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print st

    #do this in another way, a conditional statement
    st = "x is less than y" if(x < y) else "x is greater than or equal to y"
    print st
    
if __name__ == "__main__":
    main()
