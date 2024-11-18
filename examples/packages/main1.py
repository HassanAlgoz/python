import sys
import my_package
from my_package.pkg1 import module_a
from my_package.pkg2.module_a import func_a

def main():
    print(f"Hello from {__name__}")
    print(my_package.__version__)
    module_a.func_a()
    func_a()
    
    print(type(sys.argv))
    for i, a in enumerate(sys.argv):
        print(f'arg {i}: {a}')

if __name__ == "__main__":
    main()
