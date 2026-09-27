def slarge(nums):
    largest= nums[0]
    slargest= nums[0]

    for num in nums:
        if num > largest :
            slargest = largest
            largest= num

        elif num > slargest and num != largest:
            slargest = num

    return slargest

print(slarge([2,3,4]))