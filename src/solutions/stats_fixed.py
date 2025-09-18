"""A module with functions calculating various stats"""


def count(nums):
    """Returns the number of elements in an iterable"""
    return len(nums)


def total(nums):
    """Returns the total sum of an iterable of numbers"""
    return sum(nums)


def mean(nums):
    """Returns the mean, or average, of an iterable of numbers"""
    mean = total(nums) / count(nums)

    return mean


def variance(nums):
    """Returns the sample variance of an iterable of numbers"""
    squared_difference = []
    for x in nums:
        squared_difference.append((x - mean(nums)) ** 2)
    variance = sum(squared_difference) / (count(nums) - 1)

    return variance


def median(nums):
    """Return the median of an iterable of numbers"""
    sorted_nums = sorted(nums)

    # FIXME: Different behavior depending on the parity of the number of elements
    n_nums = count(nums)
    if n_nums % 2:
        # Odd number of elements
        return sorted_nums[n_nums // 2]
    return (sorted_nums[n_nums // 2] + sorted_nums[n_nums // 2 - 1]) / 2
