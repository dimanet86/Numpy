import numpy as np

def print_array(a: np.ndarray, function, msg: str, pbm: bool, *args):
    """
    Prints array before and after manipilation along with message provided
    The function parameter is a function to apply to array,
    pbm is the flag determining if we need to print array before manipulation
    """
    print(msg)
    print('-' * len(msg))
    if pbm:
        s = "Below is the array before manipulation"
        print(s)
        print('-' * len(s))
        print(a)
        s = "Below is the array after manipulation"
        print('-' * len(s))
        print(s)
        print('-' * len(s))
    if function is not None:
        print(function(a, *args))
    else:
        print(a)
    print()

# Array creation
np_array = np.random.randint(10, 100, 36).reshape(6, 6)

# Array Manipulation Functions
# Transpose Function: Create a function to transpose the array and return the result.
def transpose(array: np.ndarray) -> np.ndarray:
    return np.transpose(array).copy() # so initial array left unchanged

# Reshape Function: Develop a function to reshape the array into a new configuration (e.g., from a 6x6 matrix to a 3x12 matrix) and return the reshaped array.
def reshape(array: np.ndarray, n: int, m: int) -> np.ndarray:
    try:
        return np.reshape(array, (n, m)).copy()
    except:
        print(f'n and m must be equal to {array.shape[0] * array.shape[1]}')

# Split Function: Implement a function that splits the array into multiple sub-arrays along a specified axis and returns the sub-arrays.
def split(array: np.ndarray, sections: int, axis: int = 0) -> np.ndarray:
    return np.split(array, sections, axis).copy()

# Combine Function: Construct a function that combines several arrays into one and returns the combined array.
def combine(arrays: list, axis: int = 0) -> np.ndarray:
    return np.concat(arrays, axis).copy()

print_array(np_array, transpose, "Transpose function", 1)

print_array(np_array, reshape, "Reshape function", 1, 3, 12)

print_array(np_array, split, "Split function", 1, 3)

print_array(combine(split(np_array, 2)), None, "Combine function", 0)