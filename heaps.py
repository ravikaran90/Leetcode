import heapq

class Solution:
    def heap_operations(self,arr):
        heapq.heapify(arr)
        print("Min Heap:",arr)
        heapq._heapify_max(arr)
        print("Max Heap:",arr)

def main():
    arr=[5,10,12,3,8,15,20,25]
    obj=Solution()
    obj.heap_operations(arr)

if __name__=="__main__":
    main()