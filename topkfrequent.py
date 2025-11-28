import heapq
from collections import Counter

class Solution:
    def topkfrequent(self,nums,k):
        counts=Counter(nums)
        heap=[]
        for key,value in counts.items():
            heapq.heappush(heap,(key,value))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]


def main():
    nums=[5,12,14,17,17,17,17,17,17,8,30,30,30,50,50,50,50]
    obj=Solution()
    res=obj.topkfrequent(nums,3)
    print("Result:",res)

if __name__=="__main__":
    main()