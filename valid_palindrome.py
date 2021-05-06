# input
# "A man, a plan, a canal: panama"

# output
# true

# input
# "race a car"

# output
# false

#####
# 1 #
#####
a = "A man, a plan, a canal: Panama"
class Solution:
    def isPalidrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # 글자 or 숫자 라면 True
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): # pop(0) : 맨 앞값 / pop() 맨 뒤값
                return False
        return True

solution = Solution()
test_case : str = a
result : bool = solution.isPalidrome(test_case)
print(result)

#####
# 2 #
#####
