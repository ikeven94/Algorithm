## 자신을 제외한 배열의 곱 (Product of Array Except Self)
## 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력

# input
input = [1,2,3,4]

# output
# [24,12,8,6]

# Caution : 나눗셈 하지않고 O(n)에 풀이

######################
# 1. 왼쪽 곱 x 오른쪽 곱
#######################

def productExceptSelf(x):
    newList = []
    p = 1
    for i in range(0,len(x)):       # 왼쪽 곱
        newList.append(p)
        p = p*x[i]              
    p = 1
                                        # 왼쪽 곱 결과에 오른쪽 값 곱
    for i in range(len(x)-1,-1,-1):     # range(start,stop,step)  
        newList[i] = newList[i] * p
        p = p * x[i]
    
    return newList

print(productExceptSelf(input))

