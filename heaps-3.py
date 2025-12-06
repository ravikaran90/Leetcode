import heapq
from collections import Counter

class Solution:
    def heaps(self,nums):
        heapq.heapify(nums)
        print("Min Heap:",nums)
        heapq._heapify_max(nums)
        print("Max Heap:",nums)

    def topkfrequent(self,nums,k):
        counts=Counter(nums)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    nums=[1,1,1,1,4,4,4,3,2,2,2,5,5,9,8,7]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(nums,4)
    print("Result:",res)

if __name__=="__main__":
    main()
