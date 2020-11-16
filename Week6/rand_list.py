import random


def is_even(passed_value):
    """
    Uses modulo to see if an int is even or odd
    :param passed_value: the number to check is even
    :return: True for even, False for odd
    """
    return passed_value % 2 == 0


rand_list_int = random.sample(range(0, 101), 10)
print(rand_list_int)
print(len(rand_list_int))

for value in rand_list_int:
    if is_even(value):
        print(value, " is even")
    else:
        print(value, " is odd")
