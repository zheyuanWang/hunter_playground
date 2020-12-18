class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
            return
        if x<=self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if not self.stack: return
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack: return None
        return self.stack[-1]

    def min(self) -> int:
        if not self.min_stack:
            return
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
obj = MinStack()
obj.push(2)
obj.push(2)
obj.push(2)
obj.push(1)
obj.push(4)
obj.push(2)
print(obj.pop())
print(obj.min())
print(obj.pop())
print(obj.min())
print(obj.pop())
print(obj.min())
print(obj.pop())
print(obj.min())
print(obj.pop())