# Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    smallest = nums1 if min(len(nums1),len(nums2)) == len(nums1) else nums2
    largest = nums2 if max(len(nums1),len(nums2)) == len(nums2) else nums1

    # Option 1 - Two Dictionary approach 
    # runtime O(n * value)

    #Tradeoff - Faster Runtime, take more space
    # resultedArray=[]
    # dic_smallest={}
    # dic_largest ={}

    # for ele in smallest:
    #     if ele not in dic_smallest:
    #         dic_smallest[ele] = 1
    #     else:
    #         dic_smallest[ele] +=1

    # for ele in largest:
    #     if ele not in dic_largest:
    #         dic_largest[ele] = 1
    #     else:
    #         dic_largest[ele] +=1

    # for key, value in dic_smallest.items():
    #     if key in dic_largest.keys():
    #         if value != dic_largest[key]:
    #             minValue = min(value,dic_largest[key])
    #             for _ in range (minValue):
    #                 resultedArray.append(key)
    #         else:
    #             for _ in range(value):
    #                 resultedArray.append(key)
    
    # return resultedArray

# Tradeoff : Slower Runtime, Require less space
    #option 2
    resultedArray = []
    for i in smallest:
        if i in largest:
            resultedArray.append(i)
            largest.remove(i)
    return resultedArray


if __name__ == "__main__":
    print (intersect([4,9,5],[9,4,9,5,8,4,9]))

