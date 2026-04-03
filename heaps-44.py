import heaps

class Solution:
  def heaps(self,n):
    heaps.heapify(n)
    print("Min Heap:",n)
    heaps._max_heapify(n)
    print("Max Heap:",n)

def main():
  n=[60,63,55,52,89,4,56,90]
  obj=Solution()
  res=obj.heaps(n)

if __name__==__main__:
  main()
    
