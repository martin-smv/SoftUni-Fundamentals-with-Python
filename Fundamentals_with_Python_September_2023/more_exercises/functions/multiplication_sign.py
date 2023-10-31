def nums_less_than_zero(numbers):
    counter = 0
    for x in numbers:
        if x < 0:
            counter += 1

    return counter


def result_check(nums):
    if 0 in nums:
        return "zero"
    elif nums_less_than_zero(nums) == 1 or nums_less_than_zero(nums) > 2:
        return "negative"
    else:
        return "positive"


list_with_numbers = [int(input()) for s in range(3)]
print(result_check(list_with_numbers))