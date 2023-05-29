from collections import deque

def solution(S):
    opening_brackets = ['[','(','{']
    closing_brackets = [']',')','}']
    if len(S) == 0:
        return 1
    open_s = deque()
    for letter in S:
        if letter in opening_brackets:
            open_s.append(letter)
        else:
            closing_bracket = letter
            if len(open_s) == 0:
                return 0
            top_opening_bracket = open_s.pop()
            if closing_bracket == ')' and top_opening_bracket != '(':
                return 0
            if closing_bracket == ']' and top_opening_bracket != '[':
                return 0
            if closing_bracket == '}' and top_opening_bracket != '{':
                return 0
    if len(open_s) > 0:
        return 0
    return 1
print(solution('{[()()]}'))