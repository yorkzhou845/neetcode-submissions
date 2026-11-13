class MinStack:

    def __init__(self):
        self.data = []#all the data
        self.min = []#stores the minimum value at each level


    def push(self, val: int) -> None:
        if not self.min:#empty min
            self.min.append(val)
        elif val < (prev_min := self.min[-1]):
            self.min.append(val)
        else:
            self.min.append(prev_min)
        self.data.append(val)
    def pop(self) -> None:
        self.data.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

        
