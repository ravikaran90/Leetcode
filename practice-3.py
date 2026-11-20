import heapq

class Task_Scheduler:
    def __init__(self):
        self.heap=[]

    def add_task(self,priority,s:str):
        heapq.heappush(self.heap,(priority,s))
        print(self.heap)

    def execute_task(self):
        print("Executed Task")
        heapq.heappop(self.heap)
        print(self.heap)

def main():
    obj=Task_Scheduler()
    obj.add_task(1,"Study")
    obj.add_task(4,"Cleaning")
    obj.add_task(3,"Repair")
    obj.execute_task()
    
if __name__=="__main__":
    main()
