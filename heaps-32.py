import heapq
from collections import Counter

class Solution:
    def heaps(self,arr):
        heapq.heapify(arr)
        print("Min Heap:",arr)
        heapq._heapify_max(arr)
        print("Max Heap:",arr)
    def topkfrequent(self,nums,k):
        counts=Counter(nums)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(value,key))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    arr=[9,3,6,5,89,23,54,45,67,76,98,91,3]
    nums=[1,1,1,4,4,8,9,2,5,5]
    obj=Solution()
    obj.heaps(arr)
    res=obj.topkfrequent(nums,3)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()