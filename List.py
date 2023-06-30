class Node:
    #Node class,lets start with his constructor
    def __init__(self,value):
        self.value=value #holds the value of the node
        self.next=None   #Points to next node in the list
class Linkedlist:
    #Linkedlist class,lets start with his constructor
    def __init__(self):
        self.head=None#points to the first node in the linkelist
        #the linkedlist has a single attribute
    def display(self):
        current =self.head
        while current:
            print(current.value,"->",end=" ")
            current=current.next

    def is_empty(self):#Determine if list is empty
        return self.head is None
    
    def append(self,value):
        newNode=Node(value)#create a new node
        if self.is_empty()==True:
            self.head=newNode
        else:
            current = self.head
            while current.next is not None:  # Traverse to the last node
                current = current.next
            current.next = newNode  # Set the next reference of the last node to the new node
    def prepend(self,value,position):
        newNode=Node(value)#Create a new node
        if self.is_empty()==True:
            self.head=newNode
        else:
            current=self.head
            while current.next is not position:
                current=current.next
            current.next = newNode  # Set the next reference of the node to the position

    #def delete(value):

    #def search(value):

        

def main():
    #create an object
    list_1= Linkedlist()
    
    
    list_1.append(2)
    list_1.append(5)
    list_1.prepend(1,1)
    list_1.display()#show the list
    print("\nIs the list empty?",list_1.is_empty())
if __name__ == '__main__':
    main()