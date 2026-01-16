class Stack:
    def __init__(self):
        self.item = []

    def push(self, val):
        self.item.append(val)

    def pop(self):
        return self.item.pop()
    
    def top(self):
        return self.item[-1]
    
    def isEmpty(self):
        return len(self.item) == 0

	
	
def get_token_list(expr):
    if '**' in expr:
        print("INVALID_EXPRESSION")
        return False
    expr = expr.replace(" ", "")
    if '+' in expr: expr = expr.replace('+', ' + ')
    if '-' in expr: expr = expr.replace('-', ' - ')
    if '*' in expr: expr = expr.replace('*', ' * ')
    if '/' in expr: expr = expr.replace('/', ' / ')
    if '(' in expr: expr = expr.replace('(', ' ( ')
    if ')' in expr: expr = expr.replace(')', ' ) ')
    if '^' in expr: expr = expr.replace('^', ' ^ ')
    expr = expr.split()
    return expr

def infix_to_postfix(token_list):
    
    opstack = Stack()
    outstack = []
		
		# 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        elif token in '+-/*^':
            if opstack.isEmpty():
                opstack.push(token)
            
            elif prec[token] > prec[opstack.top()]:
                opstack.push(token)
            else:
                while prec[token] <= prec[opstack.top()]:
                    outstack.append(opstack.pop())
                    if opstack.isEmpty():
                        break
                opstack.push(token)
        else: # operand일 때
            outstack.append(token)


    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while not opstack.isEmpty():
        outstack.append(opstack.pop())


    return " ".join(outstack)
	
	
def compute_postfix(postfix):
    S = Stack()
    token_list = postfix.split()

    for token in token_list:
        if token in '+-*/^':
            later = S.pop()
            try: former = S.pop()
            except IndexError:
                print("INVALID_EXPRESSION")
                return False
            if token == '+': S.push(former + later)
            elif token == '-': S.push(former - later)
            elif token == '*': S.push(former * later)
            elif token == '/': 
                try:
                    S.push(former / later)
                except ZeroDivisionError:
                    print("ZERO_DIVISION_ERROR")
                    return False
            elif token == '^': S.push(former ** later)
        else:
            S.push(float(token))
    print(f"{S.pop():.3f}")
	
	
# 입력받아 계산기 함수들 차례로 호출
N = input()
token_list = get_token_list(N)
if token_list != False:
    compute_postfix(infix_to_postfix(token_list))