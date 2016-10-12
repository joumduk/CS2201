#Linkked List
class node:
    def __init__(self):
        self.data=None
        self.next=None
        self.prev=None

class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def list_empty(self):
        if self.head==None and self.tail==None:
            return True
        else:
            return False
        
    def list_search(self,k):
        node=self.head
        if self.list_empty():
            raise Exceoption ('List Empty')
        while node:
            if node.data==k:
                return node
            node=node.next
        return False
    def list_insert(self,x):
        new_node=node()
        new_node.data=x
        if self.list_empty():
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def list_delete(self,x):
        node=self.head
        if self.list_empty():
              raise Exceoption('List Empty')
        elif x==self.head and x==self.tail:
            self.head=None
            self.tail=None
        elif x==self.head:
            x.next.prev=None
            self.head=x.next
        elif x==self.tail:
            x.prev.next=None
            self.tail=x.prev
        else:
            node=self.head
            while node:
                if x==node:
                    x.prev.next=x.next
                    x.next.prev=x.prev
                node=node.next

#ll=linked_list()
#ll.list_insert(1)
#ll.list_insert(5)
#ll.list_insert(6)
#x=ll.list_search(5)
#ll.list_delete(x)
#print ll.head.data
#print ll.tail.data
        
