"""
Mean-Variance-Standard Deviation Calculator
"""
import numpy as np


def calculate(li):
    """
    Function that uses Numpy to output the mean, variance, standard deviation,
    max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
    """
    # Checking input
    try:
        arr = np.array(li).reshape(3, 3)
    except ValueError:
        print("List must contain nine numbers.")
        return None

    # Output
    return {
        "mean": [
            np.mean(arr, axis=0).tolist(), np.mean(
                arr, axis=1).tolist(), float(np.mean(arr))
        ],
        "variance": [
            np.var(arr, axis=0).tolist(), np.var(
                arr, axis=1).tolist(), float(np.var(arr))
        ],
        "standard deviation": [
            np.std(arr, axis=0), np.std(
                arr, axis=1).tolist(), float(np.std(arr))
        ],
        "max": [
            np.max(arr, axis=0).tolist(), np.max(
                arr, axis=1).tolist(), float(np.max(arr))
        ],
        "min": [
            np.min(arr, axis=0).tolist(), np.min(
                arr, axis=1).tolist(), float(np.min(arr))
        ],
        "sum": [
            np.sum(arr, axis=0).tolist(), np.sum(
                arr, axis=1).tolist(), float(np.sum(arr))
        ]
    }


result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
