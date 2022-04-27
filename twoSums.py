

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    
    dic ={}        
    for i,v in enumerate(nums):
        key = target-nums[i]
        if(key in dic.keys()):
            return [dic[key],i]
        else:
            dic[v] = i

if __name__ =="__main__":
   print(twoSum([3,2,4],6))
