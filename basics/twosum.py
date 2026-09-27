target = 9

seen={}

def twosum(nums, target):
    for n in nums:
        comp = target - n

    if comp in seen:
        return n, nums.get(comp)
    else:
        seen.add(n)

nums= [2,7, 3 ,2]

print(twosum(nums, target))