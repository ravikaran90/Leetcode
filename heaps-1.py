import heapq
from collections import Counter

class Solution:
    def min_max_heap(self,nums):
        heapq.heapify(nums)
        print(nums)
        heapq._heapify_max(nums)
        print(nums)
    def topkfrequent(self,nums,k):
        counts=Counter(nums)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    nums=[1,1,2,2,2,2,2,20,20,20,4,4,4,4,8,7,6]
    obj=Solution()
    obj.min_max_heap(nums)
    res=obj.topkfrequent(nums,2)
    print("Result:",res)

if __name__=="__main__":
    main()