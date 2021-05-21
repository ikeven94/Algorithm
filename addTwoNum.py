## add two numbers
## 덧셈해서 target을 만들 수 있는 2개의 숫자 return

# input
nums = [11, 2, 15, 7]
target = 9

# output
# [0, 1]

# explain
# nums[0] + nums[1] = 2 + 7 = 9

#########
# 1. BFS
#########
# 일일이 비교 >> 좋지 않은 시간 복잡도

def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]

print(twoSum(nums,target))

############
# 2. in 사용
############

def twosum2(nums,target):
    for i, n in enumerate(nums):
        complement = target - n 
        if complement in nums[i+1:]: # 앞의 target - n 이 [i+1] 번째 이후에 있다면
            return nums.index(n), nums[i+1:].index(complement) + (i+1) # n index와 

print(twosum2(nums,target))


########################
# 3. 첫번째 수 뺀 key 조회
########################

nums = [11, 2, 15, 7]
target = 9

def twosum3(nums,target):
    nums_map = {}
    # key value 바꿔서 dict에 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
        
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return nums.index(num), nums_map[target - num]


##################
# 4. 조회 구조 개선
##################

def twosum4(nums,target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num] = i
