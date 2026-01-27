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
    obj=Solution()
    nums=[67,9,8,3,7,1,45,34,90,32,89]
    arr=[1,1,1,6,6,8,4,9,3,3,3]
    obj.heaps(nums)
    res=obj.topkfrequent(arr,3)
    print("Top K Frequent:",res)

if __name__=="__main__": #Running this Python file directly
    main()