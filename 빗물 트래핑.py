## 빗물 트래핑 (Raindrop Trapping)
## 높이를 입력받아 비 온 후 얼마나 많은 물이 쌇일 수 있는지 계싼

# input
input = [0,1,0,2,1,0,1,3,2,1,2,1]

# output
# 6

################
# 1. two pointer
################

def trap(n):
    if not n:
        return 0
    
    volume = 0
    left, right = 0, len(n)-1
    left_max, right_max = n[left], n[right]

    while left < right:
        left_max, right_max = max(n[left], left_max), max(n[right], right_max)
        if left_max <= right_max:
            volume = volume + left_max - n[left]
            left = left + 1
        else:
            volume = volume + right_max - n[right]
            right = right -1
    return volume

print(trap(input))


################
# 2. stack 쌓기 
################g