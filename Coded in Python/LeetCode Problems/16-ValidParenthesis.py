class Solution:
    def isValid(self, s: str) -> bool:
        pStack = []

        for c in s:
            if c in ["(", "[", "{"]:
                # add the char to the stack
                pStack.append(c)
                continue
            if c in [")", "]", "}"]:
                # check if the most recently popped char in the stack matches
                if pStack:
                    popped = pStack.pop()
                else:
                    return False
                match c:
                    case ")":
                        if popped != "(":
                            return False
                    case "]":
                        if popped != "[":
                            return False
                    case "}":
                        if popped != "{":
                            return False
        return True if not pStack else False

    def isValid2(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


s = "["
print(Solution().isValid(s))
print(Solution().isValid2(s))