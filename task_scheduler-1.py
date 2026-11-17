import heapq

class Solution:
    def __init__(self):
        self.heap=[]
    def add_task(self,priority:int,s:str):
        heapq.heappush(self.heap,(priority,s))  
        print(self.heap)      
    #def execute_task(self,):
    #    #heappop(heap)

def main():
    obj=Solution()
    obj.add_task(4,"Do the Repair")
    obj.add_task(1,"Studying")
    obj.add_task(2,"Cleaning")
    obj.add_task(3,"Cooking")
    #heapq.heappop(obj.heap)
    
    heapq._heapify_max(obj.heap)
    print(obj.heap)
    #obj.execute_task("Execute the Repair")

if __name__=="__main__":
    main()
