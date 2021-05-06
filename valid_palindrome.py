# input
# "A man, a plan, a canal: panama"

# output
# true

# input
# "race a car"

# output
# false

#####
# 1 # 리스트로 변환
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
# 2 # 슬라이싱 사용
#####

import re
class Solution2:
    def isPalindrome2(self, s:str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s) # 숫자 or 문자 아닌것 공백처리
        return s == s[::-1] 

solution2 = Solution2()
result2 : bool = solution2.isPalindrome2(test_case)
print(result2)


