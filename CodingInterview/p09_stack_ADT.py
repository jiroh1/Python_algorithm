class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last=None

    def push(self, item):
        self.last=Node(item,self.last) #처음엔 1과 none -> 2, 1 (1=self.last

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

if __name__ == '__main__':
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    for _ in range(5):
        print(stack.pop())