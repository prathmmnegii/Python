nums= [1,2,3,5,6]
target = 9

seen = {}

def twosum(nums, target):

    for i, n in enumerate(nums):
        comp = target - n

        if comp in seen:
            return [seen[comp], i]

        else:
            seen[n] = i

    return []

print(twosum(nums, target))