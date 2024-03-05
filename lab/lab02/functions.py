# This lab teaches about functions and types in Python

# DONE: implement the function e = mc**2
def energy(mass: int) -> int:
    """calculate the energy using the mass-energy equivalence formula

    Args:
        mass (int): mass in kg

    Returns:
        int: energy in joules
    """
    c = (300_000_000**2)
    return mass * c

# TODO: add proper type hints to the function signature (weight: float, height: float) -> float
# TODO: modify the docs to specify the units of the inputs and the return value
def bmi_calc(weight, height):
    """_summary_ <-- HERE
    
    Args:
        weight (float): _description_ <-- HERE
        height (float): _description_ <-- HERE
    
    Returns:
        float: kg/m^2
    """
    return weight / (height ** 2)

# TODO: add proper type hints to the function signature
# TODO: implement the function to return the story
def story(noun, place):
    pass


# TODO: add proper type hints to the function signature
# TODO: implement the function to return the string with emojis
def emojis(s):
    pass


# TODO: add proper type hints to the function signature
# TODO: implement the function to return the sum of the two numbers (and remove the `pass` statement)
def sum_nums(a, b):
    pass


# TODO: add proper type hints to the function signature
# TODO: implement the function to add corresponding numbers in each list
def add_nums(a, b):
    pass


# this is the main function that runs when the file is executed directly
# using the command: `python functions.py`
if __name__ == "__main__":
    print(energy(1))
    pass