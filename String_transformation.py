# An in-place String Transformation

def replace_char(s,index,l):
        return s[:index]+s[index+1:]

s="a1b2c3d4e5f6g7h8i9j1k2l3m4"
#s="a1b2c3d4e5f6g7h8i9j1k2l3m4n5o6p7q8r9s1t2u3v4w5x6y7z8"

#s="a1b2c3d4e5f6g7h8i9j1k2l3m4n5o6p7q8r9s1t2u3v4w5x6y7z8" o/p-> "abcdefghijklmnopqrstuvwxyz12345678912345678912345678"

c=s[1]
#s=s.replace(c,"",1)
s=replace_char(s,1)
s+=c
for i in range(2,len(s)//2+1):
        c=s[i]
        #s=s.replace(s[i],"",1)
        s=replace_char(s,i)
        s+=c
print(s)

