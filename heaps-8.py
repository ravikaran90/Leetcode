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
    nums=[6,2,4,1,7,65,78,43,45,23,22,78,32]
    arr=[1,1,1,1,4,4,4,2,7,7,7,7,3,6,9]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,2)
    print("Result:",res)

if __name__=="__main__":
    main()


