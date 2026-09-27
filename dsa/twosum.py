nums=[2,3,8,9]
target=12

def twosum(nums, target):

    seen={}

    for i, n in enumerate(nums):
        comp = target - n

        if comp in seen:
            return [seen[comp], i]
        else:
            seen[n] = i

    return []

print(twosum(nums, target))