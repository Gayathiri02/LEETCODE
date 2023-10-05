#IMPLEMENTATION OF QUEUE USING 1STACK
class queue:
    def __init__(self):
        self.s=[]
    def enqueue(self,data):
        self.s.append(data)
    def dequeue(self):
        if not self.s:
            print("stack is empty")
        else:
            print("The dequeued element is:",self.s[0])
            self.s.pop(0)
    def front(self):
        if not self.s:
            print("stack is empty!!nothing in front position")
        else:
            print("front is:",self.s[0])
    def rear(self):
        if not self.s:
            print("stack is empty!!nothing in rear position")
        else:
            print("rear is:",self.s[-1])
    def len(self):
        if not self.s:
            print("stack is empty")
        else:
            print("length of stack is:",len(self.s))
st=queue()
st.enqueue(10)
st.enqueue(20)
st.enqueue(30)
st.dequeue()
st.front()
st.rear()
st.len()
 '''
 Enquque, front, rear,len(TC):O(1)
 Dequeue(TC):O(n)

 TIME COMPLEXITY:O(n)
 SPACE COMPLEXITY:O(1)
 '''

#IMPLEMENTING QUEUE USING 2STACKS
class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,data):
        self.s1.append(data)
    def dequeue(self):
        if not self.s1:
            print("stack is empty")
        else:
            while(self.s1):
                self.s2.append(self.s1.pop())
            print("The dequeued element is:",self.s2[-1])
            self.s2.pop()
            while(self.s2):
                self.s1.append(self.s2.pop())
            
    def front(self):
        if not self.s1:
            print("stack is empty!!nothing in front position")
        else:
            print("front is:",self.s1[0])
    def rear(self):
        if not self.s1:
            print("stack is empty!!nothing in rear position")
        else:
            print("rear is:",self.s1[-1])
    def len(self):
        if not self.s1:
            print("stack is empty")
        else:
            print("length of stack is:",len(self.s1))
st=queue()
st.enqueue(10)
st.enqueue(20)
st.enqueue(30)
st.dequeue()
st.front()
st.rear()
st.len()
'''
Enquque, front, rear,len(TC):O(1)
Dequeue(TC):O(n)

TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(1)
'''

#IMPLEMENTING QUEUE USING 2STACKS
class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,data):
        while(self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while(self.s2):
            self.s1.append(self.s2.pop())
    def dequeue(self):
        if not self.s1:
            print("stack is empty!!")
        else:
            print("Dequeued element is:",self.s1[-1])
            self.s1.pop()
    def front(self):
        if not self.s1:
            print("stack is empty!! nothing in front position")
        else:
            print("front is:",self.s1[-1])
    def rear(self):
        if not self.s1:
            print("stack is empty!! nothing to rear position")
        else:
            print("rear is:",self.s1[0])
    def len(self):
        if not self.s1:
            print("stack is empty!!")
        else:
            print("length of stack is:",len(self.s1))
st=queue()
st.enqueue(10)
st.enqueue(20)
st.enqueue(30)
st.len()
st.front()
st.dequeue()
st.front()
st.rear()
st.len()
'''
Dequque, front, rear,len(TC & SC):O(1)
Enqueue(TC & SC):O(n)

TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(n)
'''