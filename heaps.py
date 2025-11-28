import heapq
from collections import Counter

class Solution:
    def heap_operations(self,arr):
        heapq.heapify(arr)
        print("Min Heap:",arr)
        heapq._heapify_max(arr)
        print("Max Heap:",arr)

    def topkfrequent(self,nums,k):
        counts=Counter(nums)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]


def main():
    nums=[10,10,10,10,5,5,5,5,5,5,1,2,2,3]
    arr=[5,10,12,3,8,15,20,25]
    obj=Solution()
    obj.heap_operations(arr)
    res=obj.topkfrequent(nums,2)
    print("Top K Frequency:",res)    

if __name__=="__main__":
    main()