class Solution:
    def solve(self, s):
        stack = []
        op = {
            "or": lambda x, y: x or y,
            "and": lambda x, y: x and y,
        }
        for v in s.split():
            if v[0] == "(":
                stack.append(v[v.count("(") :] == "T")
            elif v.count(")") > 0:
                ct = v.count(")")
                stack.append(v[:-ct] == "T")
                for _ in range(ct):
                    right = stack.pop()
                    o = stack.pop()
                    left = stack.pop()
                    stack.append(o(left, right))
            elif v in ["T", "F"]:
                stack.append(v == "T")
            else:
                stack.append(op[v])

        if len(stack) > 1:
            for i in range(0, len(stack) - 1, 2):
                stack[i + 2] = stack[i + 1](stack[i], stack[i + 2])
            return stack[-1]

        return stack[0]
      
ob = Solution()
s = "(T or F) and (T and (F or F))"
print(ob.solve(s))