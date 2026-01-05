import heapq
from collections import Counter

class Solution:
    def heaps(self,nums):
        heapq.heapify(nums)
        print("Min Heap:",nums)
        heapq._heapify_max(nums)
        print("Max Heap")
    def topkfrequent(self,arr,k):
        counts=Counter(arr)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    nums=[50,4,67,3,89,78,12,11,14,2,70,90,35]
    arr=[1,1,1,25,25,25,6,7,7,79,79,4,2]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,3)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()