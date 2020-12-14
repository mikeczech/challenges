class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
                i += 1
            elif len(stack) > 0:
                for _ in range(len(stack)):
                    e = stack.pop()
                    if e == "(" and s[i] != ")":
                        return False
                    if e == "[" and s[i] != "]":
                        return False
                    if e == "{" and s[i] != "}":
                        return False
                    i += 1
            else:
                return False
        return True

assert Solution().isValid("()")
assert Solution().isValid("()[]")
