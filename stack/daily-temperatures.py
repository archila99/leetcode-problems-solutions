def temp(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][1]:
            stackInd, stackT = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append((i, t))
    return res

temperatures = [73,74,75,71,69,72,76,73]
print(temp(temperatures))