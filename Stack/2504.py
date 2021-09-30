import sys
input = sys.stdin.readline


s1 = []
s2 = []
score = []
s1_s, s1_m, s2_s, s2_m = 0,0,0,0

pw = input()
if pw[0] == "]" or pw[0] ==")" or  pw[-1] == "(" or pw[-1] == "[":
    print("um")
    print(0)
else:
    if pw[0] =="(":
        s1_s +=1
        s1.append(pw[0])
    if pw[0] == "[":
        s1_m +=1
        s1.append((pw[0]))
    i=1
    while(i<len(pw)):
        if(len(s1)!=len(s2)): # 성립하는 곳 찾기
            if pw[i] == "(":
                s1_s+=1
                s1.append(pw[i])
                i+=1
            if pw[i] == "[":
                s1_m+=1
                s1.append(pw[i])
                i += 1
            if pw[i] == ")":
                s2_s+=1
                s2.append(pw[i])
                i += 1
            if pw[i] == "]":
                s2_m +=1
                s2.append(pw[i])
                i += 1
        ## 점수 계산
        elif len(s1) == len(s2):
            if s1_s != s2_s or s1_m != s2_m:
                print(0)
                print("npo")
                break
            else:
                p=0
                k=s1.pop()
                if k == "(":
                    k  = 2
                if k == "[":
                    k = 3
                for i in range(1,len(s1)):
                    k = s1.pop()
                    if k == "(":
                        k = 2*k
                    if k == "[":
                        k = 3*k
                score.append(k)
                s1_s, s1_m, s2_s, s2_m = 0,0,0,0
                if i+1 == len(pw):
                    break
                if (pw[i+1] == "]" or ")"): #
                    print("ho")
                    print(0)
                else:
                    i += 1
                    if pw[i] == "(":
                        s1_s += 1
                        s1.append(pw[i])
                    if pw[0] == "[":
                        s1_m += 1
                        s1.append((pw[i]))


print(score)
