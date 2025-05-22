nums=[37,45,4,3,2,5,433,5]
i=0, j=len(nums)-1
target=37
while i<j:
    mid=i+(j-1)/2
    if nums[mid]==target:
        print(True)
        break
    elif nums[mid]<target:
        i=mid+1
    else:
        j=mid-1