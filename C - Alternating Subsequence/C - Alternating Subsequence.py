t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    chu = [nums[0]]
    res = 0

    for i in range(1, n):
        if nums[i - 1] * nums[i] > 0:
            chu.append(nums[i])
        else:
            res += max(chu)
            chu = [nums[i]]

    res += max(chu)
    print(res)
