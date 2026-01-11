import heapq
from collections import Counter

class Solution:
    def two_sum(self,nums,target):
        diction={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in diction:
                return [diction[compl],i]
            diction[nums[i]]=i

def main():
    nums=[2,4,12,16,23,32,45,50]
    obj=Solution()
    res=obj.two_sum(nums,28)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()


