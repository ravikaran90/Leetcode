import heapq
from collections import Counter

class Solution:
    def min_max_heap(self,nums):
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
    nums=[50,45,65,23,99,100,5,45,2,8,90]
    arr=[1,1,1,1,3,7,7,5,5,5,8,8,2,10,15,11]
    obj=Solution()
    obj.min_max_heap(nums)
    res=obj.topkfrequent(arr,3)
    print("Result:",res)

if __name__=="__main__":
    main()