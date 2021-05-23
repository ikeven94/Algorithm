## add three numbers
## 배열 입력 받아 합으로 0을 만들 수 있는 3개의 element

# input
nums = [-1, 0, 1, 2, -1, 4]

# output
# [
#    [-1, 0, 1],
#    [-1, -1, 2] 
# ]


#########
# 1. BFS
#########

### time out 으로 실행오류

def threeSum(nums):
    results = []
    nums.sort()
    # BFS n^3
    for i in range(len(nums)-2):
        # 중복값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1,len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))
    return results

# threeSum(nums)

################
# 2. two pointer
################

def threeSum2(nums):
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0 >> 정답
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return results

print(threeSum2(nums))
