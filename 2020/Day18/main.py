from math import ceil, floor
import datetime as dt
now = dt.datetime.now()
fin = open("input.txt", 'r')

text = [str(i) for i in fin.read().splitlines()]

n = len(text)

ans1 = 0
ans2 = 0 

i = 0
while i < n:
    equation = text[i]
    stack = []
    signs = []
    para = 0
    j = 0
    while j < len(equation):
        if equation[j] == "(":
            signs.append("(")
        elif equation[j].isnumeric():
            stack.append(int(equation[j]))
            if len(stack) > 1 and len(signs):
                if signs[-1] == "*":
                    stack[-2] = stack[-2] * stack[-1]
                    del stack[-1]
                    del signs[-1]
                elif signs[-1] == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    del stack[-1]
                    del signs[-1]
        elif equation[j] in ["*","+"]:
            signs.append(equation[j])
        elif equation[j] == ")":
            del signs[-1]
            if len(stack) > 1 and len(signs):
                if signs[-1] == "*":
                    stack[-2] = stack[-2] * stack[-1]
                    del stack[-1]
                    del signs[-1]
                elif signs[-1] == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    del stack[-1]
                    del signs[-1]
        j += 1
    ans1 += stack[-1]
    i += 1

i = 0
while i < n:
    equation = text[i]
    stack = []
    signs = []
    para = 0
    j = 0
    while j < len(equation):
        if equation[j] == "(":
            signs.append("(")
        elif equation[j].isnumeric():
            stack.append(int(equation[j]))
            if len(stack) > 1 and len(signs):
                if signs[-1] == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    del stack[-1]
                    del signs[-1]
        elif equation[j] in ["*","+"]:
            signs.append(equation[j])
        elif equation[j] == ")":
            while signs[-1] != "(":
                if len(stack) > 1 and len(signs):
                    if signs[-1] == "*":
                        stack[-2] = stack[-2] * stack[-1]
                        del stack[-1]
                        del signs[-1]
            del signs[-1]
            if len(stack) > 1 and len(signs):
                if signs[-1] == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    del stack[-1]
                    del signs[-1]
        j += 1
    while len(signs):
        if len(stack) > 1 and len(signs):
            if signs[-1] == "*":
                stack[-2] = stack[-2] * stack[-1]
                del stack[-1]
                del signs[-1]
    ans2 += stack[-1]
    i += 1

print("Part 1: ", ans1)
print("Part 2: ", ans2)
print("Time : ", dt.datetime.now()-now)