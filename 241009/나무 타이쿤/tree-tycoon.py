import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
move = ((0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1))
drug = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

for Y in range(m):
    d,l = map(int,input().split())

    # 1단계+2단계
    for i in range(len(drug)):
        drug[i][0]=(drug[i][0]+(move[d-1][0]*l))%n
        drug[i][1]=(drug[i][1]+(move[d-1][1]*l))%n
        arr[drug[i][0]][drug[i][1]]+=1
    # 3단계
    todo=[0]*len(drug)
    for i in range(len(drug)):
        for di,dj in ((1,1),(-1,-1),(-1,1),(1,-1)):
            ni,nj = drug[i][0]+di,drug[i][1]+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]>0:
                todo[i]+=1
    idx = 0
    for i,j in drug:
        arr[i][j]+=todo[idx]
        idx+=1
    # 4단계
    temp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]>=2 and [i,j] not in drug:
                arr[i][j]-=2
                temp.append([i,j])
    drug = temp[:]
ans = 0
for A in arr:
    ans+=sum(A)
print(ans)