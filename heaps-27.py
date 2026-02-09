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
  nums=[8,3,6,90,45,67,82,2,900,81]
  arr=[5,5,5,9,9,9,2,2,4,4,4,2,90,3,7,8]
  obj=Solution()
  obj.heaps(nums)
  res=obj.topkfrequent(arr,2)
  print("Top K Frequent:",res)

if __name__=="__main__":
  main()
