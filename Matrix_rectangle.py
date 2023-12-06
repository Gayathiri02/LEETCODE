r=4 
c=5
left=0
right=c
top=0
bottom=r
xo=[[0]*c for j in range(r)]
while(top<bottom):
        if(top%2==0):
            for k in range(left,right):
                xo[top][k]="X"
            top+=1
            for k in range(top,bottom):
                xo[k][right-1]="X"
            right-=1
            if(top<bottom):
                for k in range(right,left-1,-1):
                    xo[bottom-1][k]="X"
                bottom-=1
                for k in range(bottom,top-1,-1):
                    xo[k][left]="X"
                left+=1
        else:
            for k in range(left,right):
                xo[top][k]="O"
            top+=1
            for k in range(top,bottom):
                xo[k][right-1]="O"
            right-=1
            if(top<bottom):
                for k in range(right,left-1,-1):
                    xo[bottom-1][k]="O"
                bottom-=1
                for k in range(bottom,top-1,-1):
                    xo[k][left]="O"
                left+=1
for i in range(r):
    for j in range(c):
        print(xo[i][j],end=' ')
    print()
