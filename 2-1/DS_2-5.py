class Queue:
    def __init__(self):
        self.items = []
		
    def enqueue(self, val):
        self.items.append(val)
		
    def dequeue(self):
        return self.items.pop(0)
		
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return f"{self.items}"

Q = Queue()

n, k = map(int, input().split())    #O1
A = input().split()     # O1
A = list(map(int, A))   #O1

for index in range(n - k + 1):  #On
    min = 100
    for j in range(index, index + k):
        if A[j] < min: min = A[j]
    Q.enqueue(min)

B = []
for i in range(len(Q)):
    B.append(Q.dequeue())
for i in B: print(i, end=" ")

# 큐(Queue) 자료구조 사용하여 문제 해결
# 수행 시간은 O(n)