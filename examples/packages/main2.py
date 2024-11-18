import sys

def add_two(a, b):
    return a + b

def main():
    # print the type of sys.argv
    print(type(sys.argv))
    
    # print all the arguments
    for i, a in enumerate(sys.argv):
        print(f'arg {i}: {a}')
    
    # check if the user has provided the correct number of arguments
    # if not, show user how to use the program (and exit)
    if len(sys.argv) != 3:
        print('Usage: python main2.py <a> <b>')
        sys.exit(1)
    
    # read in the arguments as integers
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    
    # perform operation on arguments
    result = add_two(a, b)
    
    # show result
    print(result)

if __name__ == "__main__":
    main()
    # Example usage:
    # python main2.py 10 20