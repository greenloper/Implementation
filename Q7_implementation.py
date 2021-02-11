n=list(input())

mid=len(n)//2
sum1=0
sum2=0

for i in range(0, mid):
    sum1+=int(n[i])

for i in range(mid, len(n)):
    sum2+=int(n[i])

if sum1==sum2:
    print("lUCKY")
else: print("READY")