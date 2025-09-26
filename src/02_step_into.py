"""
Learning objectives
- Use Step Into (F11) to follow execution into functions across files.
- Inspect and navigate the Call Stack to understand where you are and how you got there.
- Recognize and fix a logic bug in a helper function.
"""

import stats


def compute_stats(nums):
    """Calculate some basic statistics"""

    total = stats.total(nums)
    count = stats.number_of_elements(nums)
    mean = stats.mean(nums)
    variance = stats.variance(nums)
    median = stats.median(nums)

    result = {
        "count": count,
        "total": total,
        "mean": mean,
        "variance": variance,
        "median": median,
    }
    return result


if __name__ == "__main__":
    data = [2, 4, 6, 8, 10]
    statistics = compute_stats(data)
    print("Numbers:", data)
    print("Stats:", statistics)

    data = [12, 2, 4, 6, 8, 10]
    statistics = compute_stats(data)
    print("Numbers:", data)
    print("Stats:", statistics)
