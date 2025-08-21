class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution: 
    def display(self,head):
        while head:
            print("Value:",head.val)
            head=head.next
    
    def middleoflinkedlist(self,head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.val

    def ifcycle(self,head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

    def reversal(self,head):
        prev=None
        current=head
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev

def main():
    head=Node(1000)
    head.next=Node(2000)
    head.next.next=Node(3000)
    head.next.next.next=Node(4000)
    head.next.next.next.next=Node(5000)
    obj=Solution()
    obj.display(head)
    mid=obj.middleoflinkedlist(head)
    print("Middle of Linked List:",mid)
    res=obj.ifcycle(head)
    print("If Cycle Exists:",res)
    newhead=obj.reversal(head)
    obj.display(newhead)

if __name__=="__main__":
    main()