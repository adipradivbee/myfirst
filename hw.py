from my_functions import *


def main():
    """
    Get user inout for 2 numbers
    print sum, diff, product and quotient
    :return: none
    """
    n1 = get_num()
    n2 = get_num()
    print('The sum of {0} and {1} is {2}'.format(n1, n2, add(n1, n2)))
    print('The diff of {0} and {1} is {2}'.format(n1, n2, diff(n1, n2)))
    print('The prod of {0} and {1} is {2}'.format(n1, n2, prod(n1, n2)))
    print('The quotient of {0} and {1} is {2}'.format(n1, n2, div(n1, n2)))
    return 0


if __name__ == '__main__':
    main()
