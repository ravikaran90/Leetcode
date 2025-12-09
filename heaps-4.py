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
    nums=[2,4,7,5,10,9,15,20,12,13,11]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(nums,2)
    print("Result:",res)

if __name__=="__main__":
    main()