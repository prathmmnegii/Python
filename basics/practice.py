# def is_even(num):
#     if num %2 ==0:
#         print("even")
#     else:
#         print("odd")

# is_even()

def find_max(nums):

    max=nums[0]

    for i in nums:
        if i > max:
            max = i

    return max

print(find_max([1,2,3,4,5]))




