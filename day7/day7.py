infile = "./input"
nums = []
for line in open(infile):
    nums = [int(x) for x in line.split(",")]

nums.sort()

a = nums[len(nums)//2]
print(a)

cost = 0
for x in nums:
    cost += abs(a - x)

print(cost)
