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
    nums=[1,1,1,1,2,2,2,2,2,3,4,5,7,7,7,12,12,12,12]
    obj=Solution()
    res=obj.topkfrequent(nums,2)
    print("Result:",res)

if __name__=="__main__":
    main()