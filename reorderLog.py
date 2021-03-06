
## log reordering
## 1. 로그 가장 앞 부분은 식별자
## 2. 문자로 구성된 로그가 숫자 로그보다 앞에
## 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로
## 4. 숫자 로그는 입력 순서대로

# input
a = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kig dig","let3 art zero"]

# output
# ["let 1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]


def reorderLog(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # print(letters,digits)
    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    # print(letters,digits)
    return letters + digits

print(reorderLog(a))

# ['let1 art can', 'let3 art zero', 'let2 own kig dig', 'dig1 8 1 5 1', 'dig2 3 6']