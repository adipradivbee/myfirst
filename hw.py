"""
Does basic arithmetic functions
on given 2 numbers and prints the
results
"""
from __future__ import print_function
from my_functions import get_num, add, diff, prod, div


def main():
    """
    Get user input for 2 numbers
    print sum, difference, product and quotient
    :return: none
    """
    first = get_num()
    second = get_num()
    print('The sum of {0} and {1} is {2}'.format(first, second, add(first, second)))
    print('The diff of {0} and {1} is {2}'.format(first, second, diff(first, second)))
    print('The prod of {0} and {1} is {2}'.format(first, second, prod(first, second)))
    print('The quotient of {0} and {1} is {2}'.format(first, second, div(first, second)))
    return 0


if __name__ == '__main__':
    main()
