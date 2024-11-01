class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.list = []

    def __len__(self):
        return len(self.list)
    
    def add(self, item):
        self.list.append(item)
        if len(self.list) > self.size:
            self.list.pop(0)

    def __getitem__(self, index):
        return self.list[index]