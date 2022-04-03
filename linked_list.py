
class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an 
    inner class.  An inner class means that its real name is related to 
    the outer class.  To create a Node object, we will need to 
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
   
        new_node = LinkedList.Node(value)  

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node      


    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        new_node = LinkedList.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node



    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """

        if self.head == self.tail:
            self.head = None
            self.tail = None
 
        elif self.head is not None:
            self.head.next.prev = None  
            self.head = self.head.next  


    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        self.tail.prev.next = None
        self.tail = self.tail.prev



    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_tail(new_value)
                
               
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       
                    new_node.next = curr.next 
                    curr.next.prev = new_node  
                    curr.next = new_node       
                return 
            curr = curr.next 


    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail: 
                    self.remove_tail()
                    return
                elif curr == self.head:
                    self.remove_head()
                    return
                else:
                    curr.next.prev = curr.prev
                    curr.prev.next = curr.next
                    return
            else:
                curr = curr.next



    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  
        while curr is not None:
            yield curr.data  
            curr = curr.next 



    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    

list = LinkedList()
list.insert_head(1)
list.insert_head(3)
list.insert_tail(1)
list.insert_after(1, 4)
list.insert_after(3, 10)
list.insert_tail(5)
list.insert_tail(6)
list.remove(10)
list.remove_tail()
print(list) #[3, 1, 4, 1, 5]
