n =int(input())

ze = [1,0]
one = [0,1]

for i in range(2,41):
    ze.append(ze[i-1]+ze[i-2])
    one.append(one[i-1]+one[i-2])

for _ in range(n):
    p = int(input())
    print(ze[p],one[p])
