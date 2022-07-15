# ver = '2022-7-15-1'

import math

# Use the following methods with:
# entry_validation_positive_numbers = root.register(mm.only_positive_numbers)
# entry_validation_positive_numbers_non_zero = root.register(mm.only_positive_numbers_non_zero)
# entry_validation_positive_numbers_comma = root.register(mm.positive_numbers_or_comma)
# entry_validation_positive_decimal_numbers = root.register(mm.positive_numbers_or_decimal)
# entry_validation_numbers_or_negative = root.register(mm.numbers_or_negative)


def hex_to_signed_int(val):
    uint_val = int(val, 16)
    bits = 4 * (len(val) - 2)
    if uint_val >= math.pow(2, bits-1):
        uint_val = int(0 - (math.pow(2, bits) - uint_val))
    return uint_val


def only_positive_numbers_2(char):
    return char.lstrip('-').isdigit()


def only_positive_numbers(char):
    if char.isdigit():
        return True
    # elif char == "":
    #     return True
    else:
        return False


def only_positive_numbers_non_zero(char):
    if char.isdigit():
        if int(char) != 0:
            return True
    if char == "":
        return True
    else:
        return False


def only_digits(char):
    return char.isdigit()


def check_float():
    try:
        # Convert it into float
        val = float(input)
        print("Input is a float  number. Number = ", val)
    except ValueError:
        print("No.. input is not a number. It's a string")


def digits_or_comma_or_minus(char):
    digit = char.isdigit()
    comma = False
    minus = False

    if char == ',':
        comma = True
    elif char == '-':
        minus = True
    else:
        comma = False

    return digit | comma | minus


def positive_numbers_or_comma(char):
    if char.isdigit():
        return True

    elif char == "":
        return True

    elif char == ",":
        return True

    else:
        return False


def numbers_or_negative(char):
    try:
        if char == "":
            return True
        elif char == "-":
            return True
        elif type(abs(int(char))) == int:
            return True
        else:
            return False
    except:
        return False


def positive_numbers_or_decimal(char):
    try:
        if char == "":
            return True
        if type(float(char)) == float:
            return True
        else:
            return False
    except:
        return False


def digits_or_space(char):
    digit = char.isdigit()
    space = char.isspace()
    return digit | space


def print_var_name(var):
    # var_name = [name for name in globals() if globals()[name] is var]
    var_name = [i for i, a in locals().items() if a == var][0]
    return var_name


def namestr(**kwargs):
    for k, v in kwargs.items():
        print("%s = %s" % (k, repr(v)))
