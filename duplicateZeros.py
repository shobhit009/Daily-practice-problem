# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]

from typing import List

def duplicateZeros( arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    if not(arr):
        return None	     
    index = 0
    while(index != len(arr)-1):
        if arr[index] == 0:
            for k in range(len(arr)-1,index+1,-1):
                arr[k] = arr[k-1]
            arr[index+1]=0
            # Checking if we have reached end of array
            if index+1 == len(arr)-1:
                break
            else:
                index = index + 2
        else:
            index = index + 1