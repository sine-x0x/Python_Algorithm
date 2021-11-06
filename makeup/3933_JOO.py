import math
# while True:
#     q = int(input())
#     if q == 0:
#         break
#     cnt = 0
#     rng = int(math.sqrt(q))
#     for i in range(1, rng + 1):
#         if i * i == q:
#             cnt += 1
#             continue
#         for j in range(i, rng + 1):
#             if i * i + j * j == q:
#                 cnt += 1
#                 break
#             elif i * i + j * j > q:
#                 break;
#             for k in range(j, rng + 1):
#                 if i * i + j * j + k * k == q:
#                     cnt += 1
#                     break
#                 elif i * i + j * j + k * k > q:
#                     break
#                 for l in range(k, rng + 1):
#                     if i * i + j * j + k * k + l * l == q:
#                         cnt += 1
#                         break
#                     elif i * i + j * j + k * k + l * l > q:
#                         break
#     print(cnt)

while True:
    q = int(input())
    if q == 0:
        break
    cnt = 0
    rng = int(math.sqrt(q))
    for i in range(1, rng + 1):
        if i * i == q:
            cnt += 1
            continue
        for j in range(i, rng + 1):
            if i * i + j * j == q:
                cnt += 1
                break
            elif i * i + j * j > q:
                break;
            for k in range(j, rng + 1):
                if i * i + j * j + k * k == q:
                    cnt += 1
                    break
                elif i * i + j * j + k * k > q:
                    break
                for l in range(k, rng + 1):
                    if i * i + j * j + k * k + l * l == q:
                        cnt += 1
                        break
                    elif i * i + j * j + k * k + l * l > q:
                        break
    print(cnt)

# def numAns(tar, ans, max, cnt):
#     curr = sum(ans)
#     if len(ans) > 8:
#         return
#     if curr > tar:
#         return
#     if curr == tar:
#         cnt += 1
#         return
#
#
#     left = tar - curr
#     ## left 보다 작은 값들에 대해 재귀문?
#     for i in range(max):
#         if arr[i] > left:
#             max = i-1
#             break
#         elif i == len(arr)-1:
#             max = j
#
#     for i in range(max+1):
#         narr = copy.deepcopy(ans)
#         narr.append(arr[i])
#         numAns(tar,copy,i,cnt)
#
#
#
# for i in buff: ## number needed to output answer
#     cnt = 0
#     max = 0
#     start = [0,0,0,0]
#     for j in range(len(arr)):
#         if arr[j] > i:
#             max = j - 1
#             break
#         elif j == len(arr) - 1:
#             max = j
#     numAns(i,start,max,cnt)
#     print(cnt)

