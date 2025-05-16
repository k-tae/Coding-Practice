def bracket(S):
    stack = []
    for ch in S:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return not stack

while True:
    A = input()
    if A == ".":
        break
    if bracket(A):
        print("yes")
    else:
        print("no")
