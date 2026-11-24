import heapq

class TaskScheduler:
    def __init__(self):
        self.heap=[]

    def add_task(self,priority,s:str)->None:
        heapq.heappush(self.heap,(priority,s))
        print("Added Task:",s)
        print("Current Ledger:",self.heap)
    
    def execute_task(self):
        popped=heapq.heappop(self.heap)
        print("Executed Task:",popped)
        print("Current Ledger:",self.heap)

def main():
    obj=TaskScheduler()
    print("Welcome to the Task Scheduler !!")
    obj.add_task(5,"Cleaning")
    obj.add_task(1,"Studying")
    obj.add_task(3,"Revision")
    obj.execute_task()
    obj.add_task(6,"Groceries")
    obj.add_task(2,"Revision")

if __name__=="__main__":
    main()
