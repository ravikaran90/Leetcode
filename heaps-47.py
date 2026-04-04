import heaps

class Solution:
  def heaps(self,n):
    heaps.heapify(n)
    print("Min Heap:",n)
    heaps._heapify_max(n)
    print("Max Heap:",n)

def main():
  n=[56,58,88,43,41,34,2,4,8,90,32]
  obj=Solution()
  obj.heaps(n)

if __name__==__main__:
  main()
