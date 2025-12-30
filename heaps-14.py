import heapq
from collections import Counter

class Solution:
    def heaps(self,arr):
        heapq.heapify(arr)
        print("Min Heap:",arr)
        heapq._heapify_max(arr)
        print("Max Heap:",arr)
    
    def topkfrequent(self,arr,k):
        counts=Counter(arr)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    arr=[1,1,1,3,3,2,5,5,5,3,4,2]
    obj=Solution()
    obj.heaps(arr)
    res=obj.topkfrequent(arr,2)
    print("Result:",res)

if __name__=="__main__":
    main()