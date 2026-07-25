class Solution:
    def isValid(self, s: str) -> bool:

        closing = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in closing:
                try:
                    if stack.pop() != closing[c]:
                        return False
                except IndexError:
                    # means we only had closing chars in the string
                    return False
            else:
                stack.append(c)

        return len(stack) == 0



