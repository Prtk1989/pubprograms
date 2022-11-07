'''

Given a 2D integer array nums where nums[i] is a non-empty array of
distinct positive integers, return the list of integers
that are present in each array of nums sorted in ascending order.

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4,
so we return [3,4].

'''
#find the common elements in all the arrays

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6],[3,4,7,6,5,1,2],[6,5,3,4,1,2,98,76]]
i = 0
intersect = [ k for k in nums[0] if k in nums[1]]  #intersection of 1st 2 elements
while i <len(nums)-1:
    intersect = [ k for k in intersect if k in nums[i+1]]   #intersection of all other elemets with 1st intersection
    i = i +1

    
print intersect


