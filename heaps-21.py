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
    arr=[1,1,1,1,9,8,2,4,7,7,7,4,4]
    nums=[8,3,90,76,9,6,2,85,45,93,7]
    obj=Solution()
    obj.heaps(nums)
    res=obj.topkfrequent(arr,2)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()