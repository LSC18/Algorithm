T = int(input())
answer = []
for i in range(T):
    H, W, N = map(int, input().split())
    N1 = N % H
    N2 = N//H + 1
    if N1 == 0:
        N1 = H
        N2 -= 1
    answer.append(int(N1)*100 + int(N2))
for j in answer:
    print(j)
