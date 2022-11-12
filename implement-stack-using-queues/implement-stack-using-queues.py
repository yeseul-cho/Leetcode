class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return []
        
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        return self.queue.popleft()

    def top(self) -> int:
        item = 0
        for _ in range(len(self.queue)):
            item = self.queue.popleft()
            self.queue.append(item)

        return item
        
    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()