# Dmytro Reshetnikov

import numpy as np

def print_array(a: np.ndarray, msg: str = ""):
    print(msg)
    print('-' * len(msg))
    print(a)

"""
Array creation    
"""
one_dim = np.arange(1, 11)
two_dim = np.arange(1, 10).reshape(3, 3)

"""
Basic operations
"""
"""
Indexing and slicing
"""
# Access and print the third element of the one-dimensional array.
print_array(one_dim[4], 'Third element of one-dim array') # Third element of one-dim array
# Slice and print the first two rows and columns of the two-dimensional array.
print_array(two_dim[0:2, 0:2], 'First two rows and cols of two-dim array') # First two rows and cols of two-dim array

"""
Basic arithmetic
"""
# Add 5 to each element of the one-dimensional array and print the result.
print_array(one_dim + 5, 'Add 5 to each element of the one-dimensional array and print the result.') 
# Multiply each element of the two-dimensional array by 2 and print the result.
print_array(two_dim * 2, 'Multiply each element of the two-dimensional array by 2 and print the result.')

# this is for commit message