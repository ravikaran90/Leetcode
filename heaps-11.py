import heapq
from collections import Counter

def heaps(nums):
    heapq.heapify(nums)
    print("Min Heap:",nums)
    heapq._heapify_max(nums)
    print("Max Heap:",nums)

def topkfrequent(arr,k):
    counts=Counter(arr)
    heap=[]
    for key,value in counts.items():
        heapq.heappush(heap,(key,value))
        while len(heap)>k:
            heapq.heappop(heap)
    return [pair[1] for pair in heap]

def main():
    nums=[45,23,89,6,2,8,19,3,6,5,1,90]
    arr=[1,1,1,1,5,5,4,3,8,9,9,3]
    heaps(nums)
    res=topkfrequent(arr,2)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()