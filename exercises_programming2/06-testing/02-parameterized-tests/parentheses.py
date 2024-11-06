def matching_parentheses(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack:
            del stack[-1]
        else:
            return False
        
    return not stack