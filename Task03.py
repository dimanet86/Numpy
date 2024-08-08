import numpy as np

# print_array function
def print_array(a: np.ndarray, msg: str = ""):
    print(msg)
    print('-' * len(msg))
    print(a)

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
        print(f'n and m must be equal {array.shape[0] * array.shape[1]}')

# Split Function: Implement a function that splits the array into multiple sub-arrays along a specified axis and returns the sub-arrays.
def split(array: np.ndarray, sections: int, axis: int = 0) -> np.ndarray:
    return np.split(array, sections, axis).copy()

# Combine Function: Construct a function that combines several arrays into one and returns the combined array.
def combine(arrays: list, axis: int = 0) -> np.ndarray:
    return np.concat(arrays, axis).copy()