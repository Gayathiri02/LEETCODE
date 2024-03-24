'''
ARRAY ADDITION:
     Given two array A[0….n-1] and B[0….m-1] of size n and m respectively, representing two numbers such that every element of arrays represent a digit.
For example, A[] = { 1, 2, 3} and B[] = { 2, 1, 4 } represent 123 and 214 respectively.
'''
#SOLUTION:
a1=[1,2,3]
a2=[2,1,4,5]
n1=''
n2=''
for i in range(len(a1)):
    n1+=str(a1[i])
for i in range(len(a2)):
    n2+=str(a2[i])
sum=int(n1)+int(n2)
print("sum is:",sum)

'''
TIME COMPLEXITY:O(n+m)
SPACE COMPLEXITY:O(n+m)
'''
