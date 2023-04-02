from collections import deque

class Stack:
    def __init__(self):
        self.box = deque()

    def push(self,value):
        self.box.append(value)
    
    def pop(self):
        return self.box.pop()
    
    def peek(self):
        return self.box[-1]
    
    def size(self):
        return len(self.box)
    
if __name__ == '__main__':
    ss = Stack()
    ss.push(5)
    ss.push(6)
    ss.push(7)
    print(ss.peek())
    print(ss.size())
