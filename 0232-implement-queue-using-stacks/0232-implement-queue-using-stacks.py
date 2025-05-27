class MyQueue:

    def __init__(self):
        self.in_st = []
        self.out_st = []

    def push(self, x: int) -> None:
        self.in_st.append(x)

    def pop(self) -> int:
        self.move()
        return self.out_st.pop()

    def peek(self) -> int:
        self.move()
        return self.out_st[-1]

    def empty(self) -> bool:
        return not self.in_st and not self.out_st

    def move(self) -> None:
        if not self.out_st:  
            while self.in_st:
                self.out_st.append(self.in_st.pop())
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()