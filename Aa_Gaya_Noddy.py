def shifting(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def rotate(l, n):
    return l[n:] + l[:n]


T=int(input())
for i in range(0,T):
    c=0
    bitsarr=input()
    bitsarr= list(map(int,bitsarr))
    for j in range(0,len(bitsarr)):
        if((shifting(bitsarr)%2)==0):
            c=c+1
        bitsarr=rotate(bitsarr,1)
    print(c)
