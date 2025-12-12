import heapq
from collections import Counter

class Solution:
    def binary_search(self,nums,target):
        left=0
        right=len(nums)
        while left<=right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
        return False

def main():
    nums=[2,4,5,6,7,8,9,15,17,23,42,62,78]
    obj=Solution()
    res=obj.binary_search(nums,42)
    print("Result:",res)

if __name__=="__main__":
    main()
