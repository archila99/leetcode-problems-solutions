def evalPRN(tokens):
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            b, a = stack.pop(), stack.pop()
            stack.append(int(a / b))  # Python 3 safe
        else:
            stack.append(int(token))
        
    return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalPRN(tokens))