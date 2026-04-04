# solving without using the map
def isValid(s):
    stack = []
    
    for char in s:
        if char == "(" or char == '{' or char == '[':
            stack.append("(")
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif char == "}":
            if not stack or stack[-1] != "{":
                return False
        elif char == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
        
        return stack == []

# solving using the map
 
def isValid2(s):
    stack = []

    mapping = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    
    return stack == []
