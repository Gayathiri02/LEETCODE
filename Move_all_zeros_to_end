'''
1) Move all non zero elements in an array to the end maintaining the non zero elements in the same order.

Input : {1, 0, 3, 0, 0, 12, 0}
Output: {1, 3, 12, 0, 0, 0, 0}
'''
#################################################Solution -1 :
arr=[1,0,3,0,0,12,0,9,100,1,0,0,0,8]
a=[]
for i in range(len(arr)):
    if(arr[i]!=0):
        a.append(arr[i])
a.extend([0]*(len(arr)-len(a)))
print(a)
'''
Time complexity :O(n)
Space complexity : O(n) 
'''
#################################################Solution-2 :
arr=[1,0,3,0,0,12,0,9,100,1]
a=arr[:]
j=0
arr.sort(reverse=True)
for i in range(len(arr)):
    if(a[i]>0):
        arr[j]=a[i]
        j+=1
print(arr) 
'''
Time complexity : O(n log n) 
Space complexity : O(n)
'''
#################################################Solution -3:
arr=[1,0,3,0,0,12,0]
for i in range(len(arr)):
    if(arr[i]==0):
        for j in range(i+1,len(arr)):
            if(arr[j]>0):
                arr[i],arr[j]=arr[j],arr[i]
                break
print(arr)
'''
Time complexity :O(n^2)
Space complexity:O(1)
'''
