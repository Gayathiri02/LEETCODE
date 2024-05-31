# Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
# The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice.
# Thus, 2 is the missing number (M) and 5 is the repeating number (R). 

arr=[6, 4, 3, 5, 5, 1]
n=6
s2=(n*(n+1))//2
s4=(n*(n+1)*((2*n)+1))//6
s1=0
s3=0
for ele in arr:
    s1=s1+ele
    s3=s3+(ele*ele)

val1=s1-s2
val2=s3-s4
# x-repeating num & y-missing number
val2=val2//val1
x=(val1+val2)//2
y=x-val1

print("Missing number is:",y," and repeating number is:",x)



