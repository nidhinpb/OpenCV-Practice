ls=list()
ls1=list()
ls2=list()
ls3=list()
temp=list()
n=int(input())
for i in range(n):
    ls1.append([input(),float(input())])
for _ in range(n-1):
    for i in range(n-1):
        if ls1[i][1] < ls1[i+1][1]:
            temp=ls1[i]
            ls1[i]=ls1[i+1]
            ls1[i+1]=temp
for i in range(n):
    ls.append(ls1[i][1])
ls2=list(sorted(set(ls)))
print(ls2)
for i in range(n):
    if ls1[i][1]==ls2[1]:
        ls3.append(ls1[i][0])
for i in sorted(ls3):
    print(i)