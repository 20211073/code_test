import sys
MAX_LEN = 20000
OFFSET = 10000
#sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())    # 건물의 층수
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[1])
#print(arr)
last_a,last_b = 0,0
ans = 1
for idx,[a,b] in enumerate(arr):
	if idx == 0:
		last_a,last_b=a,b
	if last_b < a:
		ans +=1
		last_b = b
print(ans)
