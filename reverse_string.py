# input
# ["h","e","l","l","o"]

# output
# ["o","l","l","e","h"]

# input
# ["H","a","n","n","a","h"]

# output
a =  ["h","a","n","n","a","H"]


#####
# 1 #  투 포인트 이용한 스왑
#####

def reverseString(s):
    left, right = 0 ,len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1


#####
# 2 #
#####

def reverseString2(s):
    s.reverse()


