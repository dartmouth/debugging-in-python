"""
Learning objectives
- Create and use a custom launch configuration (launch.json).
- Debug a Streamlit app launched as a Python module.
- Set breakpoints in callbacks and functions invoked by Streamlit reruns.
"""

import streamlit as st
import stats_fixed as stats


def parse_numbers(s: str):
    nums = []
    for chunk in s.split(","):
        if chunk.strip():
            nums.append(float(chunk))
    return nums


def compute_stats(nums, metrics, results={}):
    if not nums:
        return results
    if "mean" in metrics:
        results["Mean"] = stats.mean(nums)
    if "median" in metrics:
        results["Median"] = stats.median(nums)
    if "var" in metrics:
        results["Variance"] = stats.variance(nums)
    return results


def main():
    st.title("Turbo Stats")

    s = st.text_input("Enter numbers separated by commas", value="10, 12, 15, 20, 22")
    col1, col2, col3 = st.columns(3)
    to_do = []
    with col1:
        do_mean = st.checkbox("Mean", value=True)
        if do_mean:
            to_do.append("mean")
    with col2:
        do_median = st.checkbox("Median", value=True)
        if do_median:
            to_do.append("median")
    with col3:
        do_variance = st.checkbox("Variance", value=False)
        if do_variance:
            # FIXME: Use the same key here that compute_stats expects
            to_do.append("var")

    try:
        nums = parse_numbers(s)
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")
        return

    if not nums:
        st.info("Enter at least one number.")
        return

    stats = compute_stats(nums, to_do)

    if stats:
        st.subheader("Results")
        for k, v in stats.items():
            st.write(f"{k}: {v:.4g}")
    else:
        st.info("Select at least one metric to compute.")


if __name__ == "__main__":
    main()
