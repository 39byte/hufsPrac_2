class Stack:
	def __init__(self):
		self.item = []

	def push(self, val):
		self.item.append(val)

	def pop(self):
		return self.item.pop()

	def __len__(self):
		return len(self.item)

# pseudo code
def parChecker(parSeq):
	S = Stack()
	for i in range(len(parSeq)):
		if parSeq[i] == "(":
			S.push(parSeq[i])
		else:
			try:
				S.pop()
			except IndexError:
				print(False)
				return False
	if len(S) == 0: print(True)
	else: print(False)

N = list(input())
parChecker(N)