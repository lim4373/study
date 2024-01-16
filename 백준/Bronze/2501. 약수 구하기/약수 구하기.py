N, K = map(int, input().split())

num_list = []
for i in range(1, int(N**(1/2)) + 1):
    if N % i == 0:
        num_list.append(i)
        if i**2 != N:
            num_list.append(N // i)

num_list.sort()

if K > len(num_list):
    print(0)
else:
    print(num_list[K-1])
