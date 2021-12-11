infile = "./input"
nums = []
for line in open(infile):
    nums = [int(x) for x in line.split(",")]

nums.sort()

min_cost = float('inf')
for x in nums:
    cost = 0
    for y in nums:
        cost += sum(range(abs(y - x)))
    if cost < min_cost:
        min_cost = cost

print(min_cost)

# 97038219
