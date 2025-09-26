"""A module with functions calculating various stats"""


def number_of_elements(nums):
    """Returns the number of elements in an iterable"""
    return len(nums)


def total(nums):
    """Returns the total sum of an iterable of numbers"""
    return sum(nums)


def mean(nums):
    """Returns the mean, or average, of an iterable of numbers"""
    return total(nums) / number_of_elements(nums)


def variance(nums):
    """Returns the sample variance of an iterable of numbers"""
    squared_difference = []
    for x in nums:
        squared_difference.append((x - mean(nums)) ** 2)
    variance = sum(squared_difference) / (number_of_elements(nums) - 1)

    return variance


def median(nums):
    """Return the median of an iterable of numbers"""
    sorted_nums = sorted(nums)
    return sorted_nums[number_of_elements(nums) // 2]
