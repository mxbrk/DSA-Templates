class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
         temp = self.head
         while temp is not None:
                print(temp.value)
                temp = temp.next

    def append_Item(self,value):
        new_node = Node(value)
        if self.head is None:
                self.head = new_node
                self.tail = new_node
        else:
             self.tail.next = new_node
             self.tail = new_node
        self.length += 1
        return True
    
    def pop_Item(self):
        if self.head is None:
                return None
        temp = self.head
        pre = self.head
        while(temp.next is not None):
                pre = temp
                temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
                self.head = None
                self.tail = None
                return temp.value

    def prepend_Item(self, value):
        new_node = Node(value)
        if self.length == 0:
              self.head = new_node
              self.tail = new_node
        else:
              new_node.next = self.head
              self.head = new_node
              self.length += 1
              return True

    def pop_first_Item(self):
        if self.length == 0:
                return None
        temp = self.head
        self.head = self.head.next 
        temp.next = None
        self.length -= 1
        if self.length == 0:
              self.tail = None
        return temp
    
    def get_Item(self, index):
        if index < 0 or index >= self.length:
              return None  
        temp = self.head
        for _ in range(index):
              temp = temp.next
        return temp.value



main_LL = LinkedList(0)

main_LL.append_Item(1)
main_LL.append_Item(2)

main_LL.get_Item(1)
#main_LL.pop_Item()

#main_LL.prepend_Item(8)

#main_LL.pop_first_Item()

#main_LL.print_list()