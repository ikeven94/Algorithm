## 배열 파티션Ⅰ(Array Patition 1)
## n개의 pair를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수 출력

# input
input = [1,4,3,2]

# output
# 4

# min(1,2) + min(3,4) = 4

#################
# 1. 오름차순 풀이
#################

def arrayPairSum(x):
    sum = 0
    pair = []
    x.sort()

    for n in x:
        pair.append(n)
        if len(pair) == 2:
            sum = sum + min(pair)
            pair = []                # pair가 2로 찼으므로 다시 초기화 
            
print(arrayPairSum(input))

###################
# 2. 짝수번째값 계산
###################

def arrayPairSum2(x):
    sum = 0
    x.sort()
    for i, n in enumerate(x):
        if i % 2 == 0:
            sum = sum + n

    return sum

print(arrayPairSum2(input))

#####################
# 3. python 친화 방식
#####################

## 슬라이스 이용

def arrayPairSum3(x):
    return sum(sorted(x)[::2])

print(arrayPairSum3(input))    