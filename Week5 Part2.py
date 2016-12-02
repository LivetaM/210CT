class Node(object):
    def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
    def __init__(self):
         self.head=None
         self.tail=None
    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
             x.next=n.next
             n.next=x
             x.prev=n
             if x.next!=None:
                 x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x

    def delete(self, x):
         if x.prev != None: 
             x.prev.next = x.next
         else:
             self.head = x.next
         if x.next !=None:
             x.next.prev = x.prev
         else:
             self.tail = x.prev
            
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))
          
if __name__ == '__main__':
    l=List()
    node1 = Node(1)
    node3 = Node(3)
    node6 = Node(6)
    node9 = Node(9)
    l.insert(None, node3)
    l.insert(l.head,node9)
    l.insert(l.head,node1)
    l.insert(l.head,node6)
    l.delete(node1)
    l.display()


