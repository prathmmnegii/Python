def commonele(a,b):
    common=[]

    for num in a:
        if num in b and num not in common:
            common.append(num)
    return common

print(commonele([1,2,4],[2,5,7]))