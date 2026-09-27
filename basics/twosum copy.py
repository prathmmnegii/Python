target = 9
nums= [2,7, 3 ,2]


def twosum(nums, target):
    seen={}
    for n in nums:
        comp = target - n

        if comp in seen:
            return n, nums.get(comp)
        else:
            seen.add(n)

print(twosum(nums, target))

