import sys
n = int(sys.stdin.readline())
test = [sys.stdin.readline().strip() for i in range(n)]
n=2
test=['<<BP<A>>Cd-','ThIsIsS3Cr3t']

def ans(num):
    t=test[num]
    s=str()
    idx=0 #적용되는 위치

    for temp in t:
        if temp.isalnum():
            s = s[:idx] + temp + s[idx:]
            idx+=1

        elif temp=='-':
            s =  s[:idx-1] + s[idx:]
            idx-=1

        elif temp =='<':
            if idx == 0:
                pass
            else:
                idx-=1

        elif temp=='>':
            if idx >= len(s):
                pass
            else:
                idx+=1
    print(s)

ans(0)
ans(1)