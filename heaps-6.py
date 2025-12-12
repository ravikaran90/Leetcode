import heapq
from collections import Counter

class Solution:
    def heaps(self,nums):
        heapq.heapify(nums)
        print("Min Heap:",nums)
        heapq._heapify_max(nums)
        print("Max Heap",nums)
    def topkfrequent(self,arr,k):
        counts=Counter(arr)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    nums=[2,6,8,4,3,10,14,12,9,1,5]
    arr=[1,1,1,1,1,4,4,4,2,2,3,6,8,8,8,8]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,2)
    print("Result:",res)

if __name__=="__main__":
    main()
