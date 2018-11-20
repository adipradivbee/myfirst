def get_num():
    """
    Function accepts a float user input
    :return: number
    """
    good_number = False
    while not good_number:
        try:
            num = float(input('Enter the number: '))
            good_number = True
        except ValueError:
            print('Number you entered is not an integer or float')
    return num


def add(num1, num2):
    """
    Adds two numbers and returns the sum
    :param num1:
    :param num2:
    :return: num1+num2
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1+num2
    else:
        raise ValueError('integer or float needed... but got {},{}'.format(num1, num2))


def diff(num1, num2):
    """
    Returns the diff of 2 numbers
    :param num1:
    :param num2:
    :return: num1-num2
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1-num2
    else:
        raise ValueError('integer or float needed... but got {},{}'.format(num1, num2))


def prod(num1, num2):
    """
    Returns the product of 2 numbers
    :param num1:
    :param num2:
    :return: num1*num2
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1*num2
    else:
        raise ValueError('integer or float needed... but got {},{}'.format(num1, num2))


def div(num1, num2):
    """
    Returns the quotient of 2 numbers
    :param num1:
    :param num2:
    :return: num1/num2
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1/num2
    else:
        raise ValueError('integer or float needed... but got {},{}'.format(num1, num2))
