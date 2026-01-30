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
            heapq.heappush(heap,(value,key))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    nums=[4,9,8,97,100,65,3,89,43]
    arr=[2,2,2,9,9,3,4,4,4,8,8,8,8,10,6,7]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,2)
    print("Result:",res)

if __name__=="__main__":
    main()
