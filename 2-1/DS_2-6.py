class Deque:
    def __init__(self, s):
        self.items = list(s)

    def append(self, c):
        self.items.append(c)

    def appendleft(self, c):
        self.items.insert(0, c)

    def pop(self):
        return self.items.pop()
    
    def popleft(self):
        return self.items.pop(0)
    
    def __len__(self):
        return len(self.items)
    
    def right(self):
        return self.items[len(self.items)]
    
    def left(self):
        return self.items[0]
    
    def __str__(self):
        return f"{self.items}"
    
def check_palndorme(s):
    dq = Deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
            return palindrome
    return palindrome

N = input()
print(check_palndorme(N))