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
    nums=[89,43,56,3,8,9,2,67,90,6,4]
    arr=[2,2,2,9,8,5,5,5,3,4,90]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,3)
    print("Result:",res)

if __name__=="__main__":
    main()
