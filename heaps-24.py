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
    nums=[23,34,12,25,13,18,4,89,76,3,90,11]
    arr=[1,1,1,1,4,4,4,3,3,2,2,8,8,8]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,3)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()
