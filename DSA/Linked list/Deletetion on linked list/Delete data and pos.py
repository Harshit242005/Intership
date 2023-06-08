class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None


class linked_list:
    def __init__(self):
        self.head = self.tail = self.second_tail = None

    def add_node(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev = None
            return 
        else:
            self.tail.next = new_node
            new_node.next = None
            new_node.prev = self.tail
            self.second_tail = self.tail
            self.tail = new_node
            return 


    def print_nodes(self):
        temp = self.head
        if temp is None:
            return 
        else:
            while(temp):
                print(temp.data, end=" ")
                temp = temp.next


    def delete_head(self):
        temp = self.head
        if temp is None:
            return 
        else:
            self.head = temp.next
               

    def length(self):
        count = 0
        if self.head is None:
            return    
        else:
            temp = self.head
            while(temp):
                count += 1
                temp = temp.next
            return count  

    def delete_mid(self):
        if self.head is None:
            return
        else:
            mid = self.length() // 2
            return self.delete_any_node(mid) 

    # to delete the last node you have to pass the self.lenght() function it's reurn number would delete the last element 
    def delete_any_node(self, x):
        if self.head is None or x == 0:
            return
        if x > self.length():
            return 
        if x == 1:
            return self.delete_head()
        if x == self.length():
            return self.delete_last()
        else:
            temp = self.head
            i = 0
            while(i < x-1):
                
                temp = temp.next
                i += 1
            temp.prev.next = temp.next
            
        
    def delete_last(self):
        if self.head is None:
            return
        elif self.head == self.tail:
        # Special case: Only one node in the list
            self.head = self.tail = self.second_tail = None
        else:
            self.second_tail.next = None
            self.tail = self.second_tail
    
        
    
    def delete_data(self, target):
        temp = self.head
        prev = temp
        if temp is None:
            return 
        if temp.data == target:
            self.head = temp.next
            return
        if self.tail.data == target:
            return self.delete_last()
        else:
            while(temp.data != target):
                prev = temp
                temp = temp.next
             
            prev.next = temp.next   
            
l = linked_list()
for x in range(1, 11):
    l.add_node(x)
l.print_nodes()
print()
l.delete_data(5)
l.print_nodes()    