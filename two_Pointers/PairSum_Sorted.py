#commneted code is for finding all pairs that sum up to target
#uncommented code is for finding the first pair that sum up to target
#Time complexity: O(n)
#Space complexity: O(1)
from typing import List

def pairSum(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1
    #result = []
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
            #result.append([left, right])
            #left += 1
            #right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
    #return result

myList = [1, 1, 1]
target = 2
print(pairSum(myList, target))