# python3 median.py
# Enter numbers separated by spaces (or type 'upload' to upload a file): 1 1212 12 1 21 2 12 1 21 21 2 12 12 12 1 2 12 12 1 21 2 12 12 12 1 21 21 2 12
# Enter the index of the desired smallest element (0-based): 8
# Running Median of Medians...
# Median of Medians: 0.000110 seconds, Result: 2
# Running Randomized Quickselect...
# Randomized Quickselect: 0.000077 seconds, Result: 2


# test
# python3 median.py
# Enter numbers separated by spaces (or type 'upload' to upload a file): 21 2121 21
# Enter the index of the desired smallest element (0-based): 3
# Index out of bounds. Please enter a valid index.
# Enter the index of the desired smallest element (0-based): 1
# Running Median of Medians...
# Median of Medians: 0.000046 seconds, Result: 21
# Running Randomized Quickselect...
# Randomized Quickselect: 0.000048 seconds, Result: 21


#test 2
# Enter numbers separated by spaces (or type 'upload' to upload a file): 3 4
# Please provide at least 3 numbers.
# Enter numbers separated by spaces (or type 'upload' to upload a file): 3 4 5
# Enter the index of the desired smallest element (0-based): 3
# Index out of bounds. Please enter a valid index.
# Enter the index of the desired smallest element (0-based): 1
# Running Median of Medians...
# Median of Medians: 0.000266 seconds, Result: 4
# Running Randomized Quickselect...
# Randomized Quickselect: 0.000058 seconds, Result: 4

import random
import json
import csv
import os
import time

# Function to find the k-th smallest element using the Median of Medians algorithm
def median_of_medians(arr, k):
    # Base case: if the array length is 5 or less, sort and return the k-th element
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Split the array into sublists of 5 elements
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    # Calculate the median of each sublist
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    # Recursively find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the original array based on the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    # Recursively search in the appropriate partition
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

# Function to find the k-th smallest element using Randomized Quickselect
def randomized_quickselect(arr, k):
    # Base case: if the array has only one element, return it
    if len(arr) == 1:
        return arr[0]

    # Randomly choose a pivot from the array
    pivot = random.choice(arr)
    # Partition the array into elements lower and higher than the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    # Recursively search in the appropriate partition
    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return randomized_quickselect(high, k - len(low) - pivot_count)

# Function to get an array of integers from user input
def get_array_from_input():
    input_data = input("Enter numbers separated by spaces (or type 'upload' to upload a file): ").strip()
    if input_data.lower() == 'upload':
        return get_array_from_file()  # Handle file upload
    else:
        return list(map(int, input_data.split()))  # Convert input to list of integers

# Function to get an array from a file (JSON or CSV)
def get_array_from_file():
    filename = input("Enter the path to the JSON or CSV file: ").strip()
    # Check if the file exists
    if not os.path.isfile(filename):
        print("File not found. Please try again.")
        return get_array_from_file()

    # Handle JSON files
    if filename.endswith('.json'):
        with open(filename, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data  # Return the list from JSON
            else:
                print("Invalid JSON format. Please provide a JSON array.")
                return get_array_from_file()

    # Handle CSV files
    elif filename.endswith('.csv'):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.extend(map(int, row))  # Extend list with integers from the row
            return data
            
    else:
        print("Unsupported file format. Please provide a JSON or CSV file.")
        return get_array_from_file()  # Re-prompt for file input

# Function to time the execution of the selection algorithm
def time_selection_algorithm(algorithm, arr, k):
    start_time = time.time()  # Record start time
    result = algorithm(arr, k)  # Execute the selection algorithm
    end_time = time.time()  # Record end time
    return result, end_time - start_time  # Return result and time taken

if __name__ == "__main__":
    arr = get_array_from_input()  # Get the input array

    # Ensure the array has at least 3 numbers
    while len(arr) < 3:
        print("Please provide at least 3 numbers.")
        arr = get_array_from_input()

    while True:
        try:
            k = int(input("Enter the index of the desired smallest element (0-based): "))
            if 0 <= k < len(arr):
                break  # Valid index
            else:
                print("Index out of bounds. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Execute and time the Median of Medians algorithm
    print("Running Median of Medians...")
    medians_result, medians_time = time_selection_algorithm(median_of_medians, arr.copy(), k)
    print(f"Median of Medians: {medians_time:.6f} seconds, Result: {medians_result}")

    # Execute and time the Randomized Quickselect algorithm
    print("Running Randomized Quickselect...")
    quickselect_result, quickselect_time = time_selection_algorithm(randomized_quickselect, arr.copy(), k)
    print(f"Randomized Quickselect: {quickselect_time:.6f} seconds, Result: {quickselect_result}")