# variable number of non keyword arguments passed

# function definition
def high_and_low(*arguments):
    high = arguments[0]
    low = arguments[0]
    for number in arguments:

        if number > high:
            high = number

        if number < low:
            low = number


    print(high)
    print(low)


# function call
high_and_low(5, 4, 99, -5, 0)