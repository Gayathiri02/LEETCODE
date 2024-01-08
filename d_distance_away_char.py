# Rearrange a string so that all same characters become d distance away

def replace_char(res,i,char):
    return res[:i]+char+res[i+1:]

def d_distance_away_char():
    length=len(s)
    res=" "*length
    i=0
    j=0
    prev=""
    sp=False
    d={}
    d1={}
    for char in s:
        if char in d:
            d[char]+=1
        else:
            d[char]=1

    for char in d:
        count=d[char]
        if count in d1:
            d1[count].append(char)
        else:
            d1[count]=[char]
    
    keys=list(d1.keys())
    keys.sort(reverse=True)
    #print("keys:",keys)

    for count in keys:
        #if((count*(di-1))>=length):
        if(count>=length/(di-1)):
            return "Cannot be rearranged!!"
        arr=d1[count]
        for x in range(len(arr)):
            char=arr.pop(0)
            for z in range(count):
                if(prev==char):
                    if(sp):
                        space=(space+di)%length
                        res=replace_char(res,space,char)     
                    else:
                        res=replace_char(res,i,char)
                    i=(i+di)%length
                else:
                    if(res[j] in s):
                        sp=True
                        space=res.index(" ")
                        res=res.replace(" ",char,1)
                    else:
                        res=replace_char(res,j,char)
                        i=(j+di)%length
                        j+=1
                prev=char
    return res

s="geeksforgeeks"
#s="accessories"
#s="aaa" and di=2 -> o/p is cannot be rearranged
#s="aaa"
di=4
 
print(d_distance_away_char())


