import sys
n = int(sys.stdin.readline())
s1 = []
s2 = []

for _ in range(n):
    out = ""
    idx=0
    pw = sys.stdin.readline()
    for i in pw:
        if i == "<":
            out+= " " + out
        elif i == ">":
            out+= out + " "
        elif i=="-":
        else:

