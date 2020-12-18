# Write a function that returns the next answer in game fizz buzz
# Start counting in turn
# If number is divisible by 3, say 'fizz'
# If number is divisible by 5, say 'buzz'
# If number is divisible by 3 and 5, say 'fizz buzz'
# Function will always return string => convert int to str #TODO
# Annotate function and include Docstring #TODO
# Test function through loop #TODO

LOW = 1
HIGH = 100


def fizz_buzz(number: int):
    """
    Start counting in turn from start_value
    :param number: NUmber to check
    :return:If number is divisible by 3, say 'fizz'.
            If number is divisible by 5, say 'buzz'.
            If number is divisible by 3 and 5, say 'fizz buzz'.
    """
    if number % 3 == 0 and number % 5 == 0:
        return 'fizz buzz!'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return 'Try a different number than: ' + str(number)


for value in range(LOW, HIGH + 1):
    print(fizz_buzz(value))

