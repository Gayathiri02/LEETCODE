
# Given the row and the column number find the element at the given position in the pascal triangle
#                       1
#                     1   1
#                   1   2   1
#                 1   3   3   1
#               1   4   6   4   1
#             1   5   10  10  [5]  1
#           1   5  15   20  15    6   1
          
#     I/P:row=6 col=5 -> O/P: 5
#     solve using formula ncr=n!/(n!*(n-r)!)
#     eg: 10c3=10*9*8/3*2*1

def ncr(n,r):
    res=1
    for i in range(1,r):
        res=res*(n-i)
        res=res//i
    return res
n=6
r=5
print(ncr(n,r))

################################## -> T.C = O(row), S.C = O(1)
# Given the row number print all the elements in that row
# example: row=5 -> o/p: 1 4 6 4 1 
row=6
res=1
print(res)
for i in range(1,row+1):
    res=res*(row-(i-1))
    res=res//i
    print(res)

#####################################
# GIVEN NUMBER OF ROW STORE ALL THE ELEMENTS IN THE PASCAL'S TRIANGLE
res=[]
row=5   
for i in range(row):
    temp=[1]
    ans=1
    for j in range(1,i+1):
        ans=ans*(i-(j-1))
        ans=ans//j
        temp.append(ans)
    res.append(temp)
print(res)
        
        