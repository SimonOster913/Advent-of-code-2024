# Challenge 1
# line counts as "safe" if...
# 1. entries are either steadily increasing or decreasing
# 2. the difference between tow adjacent numbers is between 1 and 3
# 3. add up the sum of safe reports

# Challenge 2
# 1. delete each value in the report once
# 2. check if safe rules apply now

import numpy as np


# method for solving challenge 2
def problem_dampener(array_in, allowed_pos, allowed_neg):
    """Delete each input in report once and check if it is valid.

    Args:
        array_in (np.ndarray): report array
        allowed_pos (np.ndarray): allowed positive values (1,2,3)
        allowed_new (np.ndarray): allowed negative values (-1,-2,-3)
    """
    for idx in range(array_in.shape[0]):
        d_new_array = np.diff(np.delete(array_in, idx))

        if (
            np.isin(d_new_array, allowed_pos).all()
            or np.isin(d_new_array, allowed_neg).all()
        ):
            return True

    return False


# only these values are allowed as differences between numbers
allowed_pos = np.array([1, 2, 3])
allowed_neg = np.array([-1, -2, -3])

safe_reports = 0
with open("Day_2_input.txt") as f:
    for idx, line in enumerate(f):
        report = np.array(list(map(int, line.strip().split())))
        d_report = np.diff(report)

        # Challenge 1
        if np.isin(d_report, allowed_pos).all() or np.isin(d_report, allowed_neg).all():
            safe_reports += 1

        # Challenge 2
        elif problem_dampener(report, allowed_pos, allowed_neg):
            safe_reports += 1

print(safe_reports)
