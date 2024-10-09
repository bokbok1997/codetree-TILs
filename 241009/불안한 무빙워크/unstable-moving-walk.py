from collections import deque
n,k = map(int,input().split())
belt = list(map(int,input().split()))
belt = deque(belt)
human = deque([0]*n)
zero = 0
ans = 0
while zero<k:
    ans+=1
    belt.rotate()
    human.rotate()
    if human[n-1]==1:
        human[n-1]^=1
    for i in range(n-1,0,-1):
        if human[i-1] and belt[i]>0 and human[i]==0:
            human[i-1]^=1
            human[i]^=1
            belt[i]-=1
            if belt[i]==0:
                zero+=1
            if human[n-1]==1:
                human[n-1]^=1
    if human[0]==0 and belt[0]>0:
        human[0]^=1
        belt[0]-=1
        if belt[0]==0:
            zero+=1
print(ans)