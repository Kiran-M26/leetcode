class MyQueue(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue1)):
            ele = self.queue1[-1]
            self.queue2.append(ele)
            self.queue1.pop()
        pe = self.queue2[-1]
        self.queue2.pop()
        for i in range(len(self.queue2)):
            ele = self.queue2[-1]
            self.queue1.append(ele)
            self.queue2.pop()
        return pe

    def peek(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue1)):
            self.queue2.append(self.queue1[-1])
            self.queue1.pop()
        p = self.queue2[-1]
        for i in range(len(self.queue2)):
            self.queue1.append(self.queue2[-1])
            self.queue2.pop()
        return p

    def empty(self):
        """
        :rtype: bool
        """
        return True if(len(self.queue1) == 0) else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()