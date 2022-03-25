class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.strip("-").isnumeric():
                stack.append(t)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    stack.append(b+a)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(b*a)
                else:
                    stack.append(int(float(b)/float(a)))
        return int(stack.pop())
        