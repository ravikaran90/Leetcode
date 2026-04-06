import heaps

class Solution:
  def heaps(self,n):
    heaps.heapify(n)
    print("Min Heap:",n)
    heaps._heapify_.max(n)
    print("Max Heap:",n)
    
def main():
  n=[56,67,89,78,43,46,72,5,90,21]
  obj=Solution()
  res=obj.heaps(n)
  print("Result:",res)

if __name__==__main__:
  main()

