import heapq
from collections import Counter

class Solution:
    def heaps(self,nums):
        heapq.heapify(nums)
        print(nums)
        heapq._heapify_max(nums)
        print(nums)

    def topkfrequent(self,nums,k):
        counts=Counter(nums)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

def main():
    nums=[1,1,1,1,4,4,4,2,2,3,5,5,6,7,8]
    obj=Solution()
    obj.heaps(nums)
    topkf=obj.topkfrequent(nums,4)
    print("Top K Frequent:",topkf)

if __name__=="__main__":
    main()