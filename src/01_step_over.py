"""
Learning objectives
- Use Step Over (F10) to execute code line-by-line without diving into functions.
- Inspect and modify variables during a paused debug session.
- Evaluate expressions in the Debug Console.

"""


def compute_stats(nums):
    """Calculate some basic statistics"""

    count = len(nums)

    # Mean is total sum divided by number of elements
    total = 0
    for x in nums:
        total += x  # Step over to see total change
    mean = total / count  # Observe mean

    # Sample variance is the sum of squared differences of each number to the mean,
    # divided by number of elements - 1
    squared_difference = []
    for x in nums:
        squared_difference.append(x - mean**2)
    variance = sum(squared_difference) / (count - 1)

    result = {"count": count, "total": total, "mean": mean, "variance": variance}
    return result


if __name__ == "__main__":
    data = [2, 4, 6, 8, 10]
    stats = compute_stats(data)
    print("Stats:", stats)
