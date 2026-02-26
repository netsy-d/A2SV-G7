t  = int(input())
for _ in range(t):
    isPossible = "YES"
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n-1):
        if arr[i+1] - arr[i] > 1:
            isPossible = "NO"
            break
    print(isPossible)
