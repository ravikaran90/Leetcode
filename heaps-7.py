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
    nums=[6,8,2,4,1,35,32,34,45,42,44,62,61,4]
    arr=[1,1,1,1,4,4,4,6,6,6,7,3,2,90]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(nums,2)
    print("Result:",res)

if __name__=="__main__":
    main()