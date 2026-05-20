def subset_sum(nums, target, path=[]):
    if sum(path) == target:
        print(path)
        return
    if sum(path) > target:
        return
    for i in range(len(nums)):
        subset_sum(nums[i+1:], target, path + [nums[i]])

nums = [5,6,12,54,2,20,15]
target = 25
print("Subsets with sum =", target)
subset_sum(nums, target)