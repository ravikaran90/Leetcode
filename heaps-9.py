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
    nums=[21,5,1,4,6,2,3,8,9,5,7,23,12,45,48,32]
    arr=[1,1,1,1,6,6,6,4,4,3,9,8,12,2]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,3)
    print("Result:",res)

if __name__=="__main__":
    main()