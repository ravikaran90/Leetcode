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
    nums=[33,90,31,8,95,104,36,42,5,100,124,84]
    arr=[2,2,2,4,1,8,7,10,3,3,3,6,5]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,2)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()