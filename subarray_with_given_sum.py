# WAP to find Subarray with Given Sum
# Write a C++ function to find a subarray that sums to a given value.
# If there are multiple subarrays, return the one with the smallest starting index.
# If no such subarray exists, return an empty vector.
# Constraints:
# Example:
# Sample Input:
# 5
# 10 2 -2 -20 10
# -10
# Sample Output:
# 10 2 -2 -20
# Explanation:
# Sum of elements which return -10 which are present in the array are:
# 10 2 -2 -20
def subarray_with_given_sum(arr, target):  
    sum_map = {}  
    current_sum = 0  
    start_index = -1  # To store the start index of the best subarray  
    best_start = -1   # To store the starting index of the found subarray  
    best_end = -1     # To store the ending index of the found subarray  

    for i in range(len(arr)):  
        current_sum += arr[i]  

        # Check if the current sum equals the target  
        if current_sum == target:  
            best_start = 0  
            best_end = i  
            break  # Found subarray from index 0 to i  

        # Check if there is a subarray that sums to the target  
        if (current_sum - target) in sum_map:  
            start_index = sum_map[current_sum - target] + 1  
            if best_start == -1 or start_index < best_start:  
                best_start = start_index  
                best_end = i  

        # Store the current cumulative sum with its index  
        sum_map[current_sum] = i  

    # If a subarray is found, return it  
    if best_start != -1:  
        return arr[best_start:best_end + 1]  
    
    # If no subarray is found, return an empty list  
    return []  

# Example usage  
n = int(input("Enter the number of elements: "))  
arr = list(map(int, input("Enter the elements: ").split()))  
target = int(input("Enter the target sum: "))  

result = subarray_with_given_sum(arr, target)  

if result:  
    print(*l)  #prints elements in iterable in the form of space-separated values
