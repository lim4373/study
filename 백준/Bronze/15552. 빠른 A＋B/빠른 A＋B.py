import sys
input = sys.stdin.read
output = sys.stdout.write

# 입력 처리
data = input().split()
T = int(data[0])
results = []

# 각 테스트 케이스 계산
index = 1
for _ in range(T):
    A = int(data[index])
    B = int(data[index + 1])
    results.append(A + B)
    index += 2

# 결과 출력
output('\n'.join(map(str, results)) + '\n')
