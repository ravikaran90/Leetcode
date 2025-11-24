class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution():
    def display(self,head):
        current=head
        while current:
            print(current.val)
            current=current.next

    def mid(self,head):
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
    head=Node(100)
    head.next=Node(200)
    head.next.next=Node(300)
    head.next.next.next=Node(400)
    head.next.next.next.next=Node(500)
    obj=Solution()
    obj.display(head)
    mi=obj.mid(head)
    print("Middle Value of the Linked List:",mi)
    ifc=obj.ifcycle(head)
    print("If Cycle Exists:",ifc)
    newhead=obj.reversal(head)
    obj.display(newhead)

if __name__=="__main__":
    main()