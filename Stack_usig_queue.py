SOLUTION-1 : IMPLEMENTING STACK USING 2QUEUES
import collections
class Stack:
    def __init__(self):
        self.q1=collections.deque()
        self.q2=collections.deque()
    def push(self,data):
        if not self.q1:
            self.q1.append(data)
        while self.q1:
            self.q2.append(self.q1.pop())
        self.q1.append(data)
        while(self.q2):
            self.q1.append(self.q2.pop())
    def pop(self):
        if not self.q1:
            print("stack is empty!!")
        else:
            return self.q1.popleft()
    def top(self):
        if self.q1:
            return self.q1[0]
        print("stack is empty nothing to print!!")
        return
    def size(self):
        return(len(self.q1))
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("initial stack size is:",s.size()-1)
print("stack is:")
for ele in range(s.size()):
    print(s.top())
    s.pop()
print(s.top())
print("stack size is:",s.size())
print(s.pop())
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(n)
#################################################################
SOLUTION-2 : IMPLEMENTING STACK USING 2QUEUES
from collections import deque
class Stack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
    def push(self,data):
        self.q2.append(data)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1
    def pop(self):
        if not self.q1:
            print("stack is empty!! nothing to pop")
        else:
            self.q1.popleft()
    def top(self):
        if not self.q1:
            print("stack is empty!! nothing to display")
        else:
            print(self.q1[0])
    def size(self):
        print("size of stack is:",len(self.q1))
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.size()
for i in range(len(s.q1)):
    s.top()
    s.pop()
s.pop()
s.top()
s.size()
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(1)
#################################################################
SOLUTION-3 : IMPLEMENTING STACK USING 1 QUEUE
from collections import deque
class Stack():
    def __init__(self):
        self.q=deque()
    def push(self,data):
        if not self.q:
            self.q.append(data)
        else:
            self.q.append(data)
            l=len(self.q)
            for i in range(l):
                self.q.append(self.q.popleft())
    def pop(self):
        if not self.q:
            print("stack is empty!! nothing to pop")
        else:
            return self.q.popleft()
    def top(self):
        if not self.q:
            return("Nothing to see here stack is empty!!")
        else:
            return self.q[0]
    def size(self):
        return len(self.q)
s=Stack()
print("initial size of stack is:",s.size())
print("stack is:")
s.push(10)
s.push(20)
s.push(30)
for ele in range(s.size()):
    print(s.top())
    s.pop()
print(s.pop())
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(1)
#################################################################
SOLUTION-4 : IMPLEMENTING STACK USING 1 QUEUE
import queue
stack=queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
#stack.put(40,timeout=1)
print("stack size is:",stack.qsize())
print(stack.get())
print(stack.get())
print(stack.get())
#stack.get(timeout=1)
print("stack size is:",stack.qsize())
stack.put(40)
print("stack is empty:",stack.empty())
TIME COMPLEXITY:O(1)
SPACE COMPLEXITY:O(1)
