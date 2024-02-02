#probability_range
#initial values
minimum_value = 0
maximum_value = 100
low_value = 20
high_value = 80

def probability_range_improved(low_range, high_range, minimum, maximum):

    if isinstance(low_range, str) or isinstance(high_range, str):
        print('Inputs should be numbers not strings')
        return None

    if low_range < minimum or low_range > maximum:
        print('Your low range value must be between minimum and maximum')
        return None

    elif high_range < minimum or high_range > maximum:
        print('The high range value must be between minimum and maximum')
        return None

    else:
        probability = abs(high_range - low_range) / (maximum - minimum)
        return probability



result = probability_range_improved(low_value, high_value, minimum_value, maximum_value)

if result is not None:
    print(f"The probability in the specified range is: {result}")