import numpy as np

def print_array(a: np.ndarray, function, msg: str, pbm, *args):
    """
    Prints array before and after manipilation along with message provided
    The function parameter is a function to apply to array,
    pbm is the flag determining if we need to print array before manipulation
    """
    if pbm:
        print(msg)
        print('-' * len(msg))
        s = "Below is the array before manipulation"
        print(s)
        print('-' * len(s))
        print(a)
    print(msg)
    print('-' * len(msg))
    if function is not None:
        print(function(a, *args))
    else:
        print(a)

"""
Data I/O Functions
"""
# Save Function: Create a function to save the array to a text file, a CSV file, and a binary format (.npy or .npz).
def save(arr: np.ndarray, path: str, format: str):
    match format:
        case 'b' | 'bin' | 'binary':
            np.save(path, arr)
        case 't' | 'txt' | 'text':
            np.savetxt(path, arr)
        case 'c' | 'csv':
            np.savetxt(path, arr, delimiter=',')
        case _:
            print('Please choose either binary, text or csv format.')

# Load Function: Develop a function to load the array from each of the saved formats back into NumPy arrays.
def load(path: str, format: str='') -> np.ndarray:
    match format:
        case 'b' | 'bin' | 'binary':
            return np.load(path)
        case 't' | 'txt' | 'text':
            return np.loadtxt(path)
        case 'c' | 'csv':
            return np.loadtxt(path, delimiter=',')
        case _:
            print('Please choose either binary, text or csv format.')


"""
Aggregate Functions
"""
# Summation Function: Create a function to compute the summation of all elements.
def summation(arr: np.ndarray, axis = None) -> np.int64:
    return np.sum(arr, axis).copy()

# Mean Function: Develop a function to calculate the mean of the array.
def mean(arr: np.ndarray, axis = None) -> np.float64:
    return np.mean(arr, axis).copy()

# Median Function: Implement a function to find the median of the array.
def median(arr: np.ndarray, axis = None) -> np.float64:
    return np.median(arr, axis).copy()

# Standard Deviation Function: Construct a function to calculate the standard deviation of the array.
def sd(arr: np.ndarray, axis = None) -> np.float64:
    return np.std(arr, axis).copy()

"""
Axis-Based Aggregate Functions: Create functions to apply these aggregate operations along different axes (row-wise and column-wise).
"""
# This task is implemented as a part of initial task
# All function signatures contain axis parameter, which defaults to None
# if one needs to run any function above along any axis, then axis may be supplied as keyword argument 

"""
Manipulation workflow
"""
# Array creation and saving
test_array = np.random.randint(10, 99, 100).reshape(10, 10)
save(test_array, 'D:\\binary_array', 'b')
save(test_array, 'D:\\text_array.txt', 't')
save(test_array, 'D:\\csv_array.csv', 'c')

# Loading and printing binary file
binary = load('D:\\binary_array.npy', 'b')
print_array(binary, function=None, msg="Loaded binary array: ", pbm=False)

# Loading and printing text file
text = load('D:\\text_array.txt', 't')
print_array(text, function=None, msg="Loaded text array: ", pbm=False)

# Loading and printing csv file
text = load('D:\\csv_array.csv', 'c')
print_array(text, function=None, msg="Loaded csv array: ", pbm=False)

"""
Aggregate Computation and Reporting
"""
# Summation function
print_array(test_array, summation, "Result of the summation function", True)

# Mean function
print_array(test_array, mean, "Result of the mean function", True)

# Median function
print_array(test_array, median, "Result of the median function", True)

# Standard deviation function
print_array(test_array, sd, "Result of the standard deviation function", True)

"""
Execution of the above function along axis = 1
"""
# Summation function
print_array(test_array, summation, "Result of the summation function", True, 1)

# Mean function
print_array(test_array, mean, "Result of the mean function", True, 1)

# Median function
print_array(test_array, median, "Result of the median function", True, 1)

# Standard deviation function
print_array(test_array, sd, "Result of the standard deviation function", True, 1)