import heapq
from collections import Counter

class Solution:
    def heaps(self,nums):
        heapq.heapify(nums)
        print("Min Heap:",nums)
        heapq._heapify_max(nums)
        print("Max Heap:",nums)
    def topkfrequent(self,arr,k):
        counts=Counter(arr)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    nums=[45,32,40,31,3,89,5,76,2,44,90,1,85,41]
    arr=[2,2,2,4,4,5,6,1,8,6,9,9,9,10,14,3]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,3)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()
