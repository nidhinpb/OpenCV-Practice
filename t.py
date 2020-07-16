'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
ls=list(map(int,input().split()))
ls.sort()
print(sum(ls)/10)
if n%2==0:
    print((ls[n//2]+ls[(n//2)-1])/2)
else:
    print(ls[(n+1)/2])
d= dict()
ls2=list()
for i in ls:
    d[i]=ls.count(i)
for i in d:
    if d[i]==max(d.values()):
        ls2.append(i)
print(ls[0])
'''
n = int(input())
arr=list(map(int, input().split()))
arr.sort()
s=set(arr)
print(list(s)[len(s)-2])