from collections import deque

n=int(input())
k=int(input())
apple=[]
for i in range(k):
    apple.append(list(map(int, input().split())))
l=int(input())
rotate=[]
for i in range(l):
    rotate.append(list(map(str, input().split())))

time=0
snake_locate=[[0]*(n+1) for _ in range(n+1)]
snake_locate[1][1]=1
snake_head=[1, 1]

direction=[[0, 1], [1, 0], [0, -1], [-1, 0]]
q=deque()
q.append([1,1])
now_direction=0

while(True):
    time+=1
    for r in rotate:
        if time==int(r[0]):
            if r[1]=='L':
                now_direction-=1
                if now_direction==-1:
                    now_direction=3
            else:
                now_direction+=1
                if now_direction==4:
                    now_direction=0

    snake_head[0]+=direction[now_direction][0]
    snake_head[1]+=direction[now_direction][1]
    if snake_head[0]<0 or snake_head[0]>n or snake_head[1]<0 or snake_head[1]>n:
        break

    if snake_locate[snake_head[0]][snake_head[1]] == 1: break

    for a in apple:
        if snake_head[0] == a[0] and snake_head[1] == a[1]:
            delete = q.popleft()
            snake_locate[delete[0]][delete[1]] = 0

    hx=snake_head[0]
    hy=snake_head[1]
    q.append([hx,hy])
    snake_locate[snake_head[0]][snake_head[1]] = 1

print(time+1)