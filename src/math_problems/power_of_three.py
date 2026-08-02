from sys import maxsize


def power_of_three(number: int) -> bool:
    """Power of Three.

    Given an integer, write a function to determine if it is a power of three.
    """
    int_32_max = 1162261467
    int_64_max = 4052555153018976267

    if maxsize > int_32_max:
        return number > 0 and int_64_max % number == 0
    return number > 0 and int_32_max % number == 0
