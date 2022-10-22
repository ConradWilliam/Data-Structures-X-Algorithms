def bubblesort(nums):
    x = len(nums)-1
    for i in range (x,0,-1):# For every value in the list
        for j in range(i):
            status = False
            if nums[j]>nums[j+1]: #if value in list is greater than value directly to the right of it,
                nums[j],nums[j+1] = nums[j+1],nums[j]#Switch these values
                status = True
        if not status:
            break   

nums=[1, 6, 5, 2]
bubblesort(nums)
print(nums)