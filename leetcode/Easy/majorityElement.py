def majorityElement(nums):
    ele,count = 0,0
    for num in nums:
        if num == count:
            count += 1
        elif num == 0:
            ele,count = num,1
        else:
            count -= 1
    return ele
