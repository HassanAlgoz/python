

def my_function():
    print("Hello from my_module!")
    
class MyClass:
    def __init__(self):
        print("An instance of MyClass was created!")

my_variable = 99


# __name__ is a special built-in variable that is set to the name of the module
# when the module is run directly. If the module is being imported, then __name__
# is set to the name of the module: `my_module` in this case.
if __name__ == '__main__':
    # This will only run if my_module is the main file being run!
    # Not if it is being imported as a module
    print('I am my_module and I am being run directly!')