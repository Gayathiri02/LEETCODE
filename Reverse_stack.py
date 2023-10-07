#REVERSE A STACK WITHOUT USING FOR LOOPS
#SOLUTION-1
s=[1,2,3,4,5]
res=[]
def reverse(s):
    if(len(s)==0):
        print(res)
        return
    else:
        res.append(s.pop())
        reverse(s)
reverse(s)
'''
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(n)
'''

#SOLUTION-2
stack=[1,2,3,4,5,6,7]
print(list(reversed(stack)))

'''
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(1)
'''

#SOLUTION-3
stack=[5,6,7,8,9]
stack.reverse()
print(stack)
'''
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(1)
'''

#SOLUTION-4
s=[10,20,30,40,50]
print(s[::-1])
'''
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(n)
'''
