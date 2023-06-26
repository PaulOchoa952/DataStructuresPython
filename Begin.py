class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):#Determine if stack is empty
        return len(self.items)==0
    
    def push(self,item):#push method
        self.items.append(item)

    def pop(self):#pop method
        if not self.is_empty():
            return self.items.pop()
    def peek(self):#peek method,look for the element in the stack´s top
        if not self.is_empty():
            return self.items[-1]        
    def size(self):#return the size
        if not self.is_empty():
            return len(self.items)
        
def main():
    S1= Stack()
    S1.push(12)
    S1.push(11)
    #print(S1.size())
    print(S1.peek())
    #S1.pop()
    print("Popped",S1.peek())
if __name__ == '__main__':
    main()