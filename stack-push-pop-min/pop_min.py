class Stack:
    def __init__(self):
        # Your subclass must not access this attribute
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


class StackWithMin(Stack):
   # Create whatever methods you need
    def __init__(self):
        self.min = []
        self._items = []
        
    def push(self, value):
        if(len(self.min) == 0):
            self.min.append(value)
        elif(self.min[-1]>=value):
            self.min.append(value)

        self._items.append(value)

    def pop(self):
        if(self._items[-1] == self.min[-1]):
            self.min.pop()
        return self._items.pop()

    def minimum(self):
        # You must implement at least this method
        # AND it must be O(1) time
        return self.min[-1]