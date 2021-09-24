import sys
n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()
for i in a:
    print(i)

# def qs(low, high, arr):
#     if high <= low:
#         return
#     i = low
#     j = high
#     pivot = arr[(low + high) // 2]
#
#     while (i <= j):
#         while (arr[i] < pivot):
#             i += 1
#         while (arr[j] > pivot):
#             j -= 1
#         if (i <= j):
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#
#     qs(low, j, arr)
#     qs(i, high, arr)

# def qs(arr):
#     def sort(low,high):
#         if high <= low:
#             return
#
#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)
#
#     def partition(low,high):
#         pivot = arr[(low+high)//2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low +1, high-1
#         return low
#
#     return sort(0,len(arr)-1)


qs(0,n-1,a)
for i in a:
    print(i)

'''
처음 [5,4,3,2,1]에서 low = 0 high = 4
arr[low],[high] 조건을 모두 만족하기 때문에 [1,4,3,2,5]로 변경
return low = 1
다음 밑에 sort(0, mid -1 = 0 ) 이 부분은 if 문 조건 만
다음 밑에 sort(1, 4) 실행 
pivot은 3
low = 1, high =3
바꾸면 
[1,2,3,4,5]
low = 2 high =2
그러면 mid =  return low =2
밑에 sort (1,1)
sort(2,4)
=> 얘는 바꿀게 없어서 pivot index 인 3에서 만남 
 low = 4 high = 2로 끝 
 끝끝
'''