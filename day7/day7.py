infile = "./input"
nums = []
for line in open(infile):
    nums = [int(x) for x in line.split(",")]

nums.sort()

min_cost = float('inf')
for x in range(max(nums)):
    cost = 0
    for y in nums:
        if y != x:
            n = abs(y-x)
            cost += (n * (n + 1))//2
    if cost < min_cost:
        min_cost = cost

print(min_cost)
