# import sys
# input = sys.stdin.readline
#
#
# s1 = []
# s2 = []
# score = []
# s1_s, s1_m, s2_s, s2_m = 0,0,0,0
#
# pw = input()
# if pw[0] == "]" or pw[0] ==")" or  pw[-1] == "(" or pw[-1] == "[":
#     print("um")
#     print(0)
# else:
#     if pw[0] =="(":
#         s1_s += 1
#         s1.append(pw[0])
#     if pw[0] == "[":
#         s1_m += 1
#         s1.append((pw[0]))
#     i=1
#     while(i<len(pw)):
#         if(len(s1)!=len(s2)): # 성립하는 곳 찾기
#             if pw[i] == "(":
#                 s1_s+=1
#                 s1.append(pw[i])
#                 i+=1
#             if pw[i] == "[":
#                 s1_m+=1
#                 s1.append(pw[i])
#                 i += 1
#             if pw[i] == ")":
#                 s2_s+=1
#                 s2.append(pw[i])
#                 i += 1
#             if pw[i] == "]":
#                 s2_m +=1
#                 s2.append(pw[i])
#                 i += 1
#         ## 점수 계산
#         elif len(s1) == len(s2):
#             if s1_s != s2_s or s1_m != s2_m:
#                 print(0)
#                 print("npo")
#                 break
#             else:
#                 p=0
#                 k=s1.pop()
#                 if k == "(":
#                     k  = 2
#                 if k == "[":
#                     k = 3
#                 for i in range(1,len(s1)):
#                     k = s1.pop()
#                     if k == "(":
#                         k = 2*k
#                     if k == "[":
#                         k = 3*k
#                 score.append(k)
#                 s1_s, s1_m, s2_s, s2_m = 0,0,0,0
#                 if i+1 == len(pw):
#                     break
#                 if (pw[i+1] == "]" or ")"): #
#                     print("ho")
#                     print(0)
#                 else:
#                     i += 1
#                     if pw[i] == "(":
#                         s1_s += 1
#                         s1.append(pw[i])
#                     if pw[0] == "[":
#                         s1_m += 1
#                         s1.append((pw[i]))
#
#
# print(score)

import sys
input = sys.stdin.readline
pw = input().strip()

# if pw[0] == "]" or pw[0] == ")" or pw[-1] == "(" or pw[-1] == "[":
#     print(0)
#     sys.exit()
#
# s1_s, s1_m, s2_s, s2_m = 0,0,0,0
# for i in pw:
#     if i == "(":
#         s1_s += 1
#     elif i == "[":
#         s1_m += 1
#     elif i == ")":
#         s2_s += 1
#     elif i == "]":
#         s2_m += 1
stack1=[]
for s in pw:
    if s == '(' or s == '[':
        stack1.append(s)
    elif s == ')' and stack1:
        if stack1[-1] == '(':
            stack1 = stack1[:-1]
        else:
            stack1.append(s)
    elif s == ']' and stack1:
        if stack1[-1] == '[':
            stack1 = stack1[:-1]
        else:
            stack1.append(s)
    else:
        stack1.append(s)

if stack1:
    print(0)
else:
    stack = []
    for s in pw:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2 # 속 알맹이 ()
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = tmp * 2
                        break
                    else: # 점수가 나온 경우 tmp에
                        tmp += stack[i]
                        stack = stack[:-1]
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3 # 속 알맹이 []
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[i] # 점수가 나온경우 tmp에
                        stack = stack[:-1]
    score = 0
    for i in stack:
        score += i
    print(score)
