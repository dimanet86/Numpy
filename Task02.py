import numpy as np
import random as rd
import math

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

"""
Array creation
"""
# helper dict, containing ids and prices of goods
ids_and_price = {
    156: 100.0, 
    111: 99.2,
    258: 88.0,
    655: 75.5,
    877: 65.0,
    112: 55.7,
    416: 123,
    587: 34.5,
    999: 45.6
}

# Sub-arrays used to construct main np array
transaction_id = np.arange(100) # 0
user_id = np.random.randint(100, 999, 100) # 1
product_id = [rd.choice(list(ids_and_price.keys())) for i in range(100)] # 2
quantity = [rd.randint(0, 1000) for i in range(100)] # 3
price = [ids_and_price[i] for i in product_id] # 4
timestamps = np.array(np.random.randint(1702944000, 1712944000, 100), dtype='datetime64[s]') # 5

# collecting the entire array
transactions = np.array([transaction_id, user_id, product_id, quantity, price, timestamps])

"""
Data Analysis Functions
"""
# Total revenue function
def total_revenue(transactions: np.ndarray) -> float:
    return np.round(np.sum(transactions[3] * transactions[4]), 2)

# Number of unique users made transactions
def unique_users(transactions: np.ndarray) -> int:
    return np.unique(transactions[1]).size

# Most purchased product based on quantity sold
# Returns product_id  
def most_purchased(transactions: np.ndarray) -> tuple: 
    index_max = np.argmax(transactions[3])
    return transactions[2, index_max]

# Type Casting and Checking Functions
# Function to convert the price array from float to integer.
def float_to_int(transactions: np.ndarray) -> np.ndarray:
    return transactions[4].astype(np.int32) # let's take array of floats

# Develop a function to check the data types of each column in the array.
# dtype gives dtype = object for homegeneous sub-arrays for some reason
def check_types(transactions: np.ndarray): 
    types = [row.dtype for row in transactions]
    return types

print(check_types(transactions))

"""
Array Manipulation Functions
"""
# Product Quantity Array Function: Create a function that returns a new array with only the product_id and quantity columns.
def quantity_array(transactions: np.ndarray) -> np.ndarray:
    return np.array([transactions[2].copy(), transactions[3].copy()])

# User Transaction Count Function
# Returns tuple of sequences: first sequence is users ids corresponding to each transaction,
# second is the array of numbers of occurences of each user id
def transaction_count(transactions: np.ndarray) -> tuple:
    return np.unique(transactions[1], return_counts=True)

# Masked Array Function
def masked(transactions: np.ndarray) -> np.ndarray:
    # return transactions[:, transactions[3] == 0].copy()
    return np.ma.array(transactions, 
                       mask=[[transactions[3] == 0], 
                             [transactions[3] == 0], 
                             [transactions[3] == 0], 
                             [transactions[3] == 0], 
                             [transactions[3] == 0], 
                             [transactions[3] == 0]])

"""
Arithmetic and Comparison Functions
"""
# Price Increase Function
# Value represents increase percentage 
def price_increase(transactions: np.ndarray, value: np.int32) -> np.ndarray:
    return transactions[4].copy() * (1 + value / 100)

# Filter Transactions Function: Implement a function to filter transactions to only include those with a quantity greater than 1.
def filter_trans(transactions: np.ndarray) -> np.ndarray:
    return transactions[:, transactions[3] > 1].copy()

# Revenue Comparison Function: Create a function to compare the revenue from two different time periods.
def comparison_tp(transactions: np.ndarray, 
                  fpstart: str, 
                  fpend: str,
                  spstart: str, 
                  spend: str
                  ) -> float:
    fpstart = np.datetime64(fpstart)
    fpend = np.datetime64(fpend)
    spstart = np.datetime64(spstart)
    spend = np.datetime64(spend)
    
    mask_first_left = transactions[5] >= fpstart 
    mask_first_right = transactions[5] <= fpend 
    mask_first = mask_first_left & mask_first_right

    mask_second_left = transactions[5] >= spstart 
    mask_second_right = transactions[5] <= spend 
    mask_second = mask_second_left & mask_second_right

    fptrans = transactions[:, mask_first]
    sptrans = transactions[:, mask_second]

    fptrans_rev = np.sum(fptrans[3] * fptrans[4])
    sptrans_rev = np.sum(sptrans[3] * sptrans[4])

    if fptrans_rev > sptrans_rev:
        print(f'Revenue of first time period is higher than of second time period')
        return fptrans_rev
    else:
        print(f'Revenue of second time period is higher than of first time period')
        return sptrans_rev

"""
Indexing and Slicing Functions
"""
# User Transactions Function: Create a function to extract all transactions for a specific user.
def extract_user(transactions: np.ndarray, user_id: int) -> np.ndarray:
    return transactions[:, transactions[1] == user_id]

extract_user(transactions, 949)

# Date Range Slicing Function: Develop a function to slice the dataset to include only transactions within a specific date range.
def slice_time(transactions: np.ndarray, 
                  start: str, 
                  end: str
                  ) -> np.ndarray:
    start = np.datetime64(start)
    end = np.datetime64(end)
    
    mask_first_left = transactions[5] >= start 
    mask_first_right = transactions[5] <= end 
    mask_first = mask_first_left & mask_first_right
    trans = transactions[:, mask_first]
    return trans

# Top Products Function: Implement a function using advanced indexing to retrieve transactions of the top 5 products by revenue.
# NB: I know that this function returns top five products sorted by transaction's revenue,
# but I cannot come up with something more reasonable
def top_five_prods(transactions: np.ndarray) -> np.ndarray:
    z = np.argsort(transactions[3] * transactions[4])
    return transactions[:, z][2,-5:].copy()

"""
Manipulation workflow
"""
result = total_revenue(transactions)
print(f'Total revenue = {result}')

result = unique_users(transactions)
print(f'Number of unique users is {result}')

result = most_purchased(transactions)
print(f'The most purchased is the product with id {result}')

result = float_to_int(transactions)
print_array(result, function=None, msg="Array converted to int", pbm=1)

result = check_types(transactions)
print(result)

result = quantity_array(transactions)
assert result.shape == (2, 100)
print_array(result, function=None, msg="Product quantity array function", pbm=0)

result = transaction_count(transactions)
print_array(result, function=None, msg="Transaction count function", pbm=0)

result = masked(transactions=transactions)
assert len(result.shape) == 2
print_array(result, function=None, msg="Masked array function", pbm=1)

result = price_increase(transactions, 10)
assert result.shape == (2, 100)
print_array(result, function=None, msg="Price increase function", pbm=1)

result = filter_trans(transactions)
print(result.shape)
print_array(result, function=None, msg="Filter transactions function", pbm=1)

result = comparison_tp(transactions, '2023-01-01T00:00', '2024-01-01T00:00', '2023-01-01T00:00', '2025-11-01T00:00')
print(f'Revenue comparison function result {result}')

result = extract_user(transactions, 205)
print_array(result.T, function=None, msg="User Transaction function", pbm=0)

result = slice_time(transactions, '2023-01-01T00:00', '2024-01-01T00:00')
print_array(result.T, function=None, msg="Date Range Slicing function", pbm=0)

result = top_five_prods(transactions)
print_array(result.T, function=None, msg="Top Five Products function", pbm=0)