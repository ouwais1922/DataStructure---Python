#In LinkedList class that we implemented in code01 add following two methods:
#def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
#def remove_by_value(self, data):
    # Remove first node that contains data
class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Your linkedlist is empty")
            return
        itr = self.head
        Strign = ''
        while itr:
            Strign += str(itr.data) + '-->'
            itr = itr.next
        print(Strign)

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data,None)
        itr.next = node

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count = count +1
            itr = itr.next
        return count
    
    def remove_index(self,index):
        if index <0 or index> self.length():
            raise Exception("Invalid instruction")
        
        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count = count + 1
            itr = itr.next

    def add_index(self,index,data):
        if index<0 or index > self.length():
            raise Exception("Invalid instructuon")
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
               node = Node(data,itr.next)
               itr.next = node 
            count +=1
            itr =itr.next

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next
    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") 
    ll.print()
    ll.remove_by_value("mango")
    ll.print()

