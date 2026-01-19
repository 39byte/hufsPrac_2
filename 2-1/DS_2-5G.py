class Deque:
    def __init__(self):
        self.items = []
        
    def push_back(self, val):
        """뒤쪽에 데이터 추가"""
        self.items.append(val)
        
    def pop_back(self):
        """뒤쪽 데이터 제거 및 반환"""
        if not self.is_empty():
            return self.items.pop()
            
    def pop_front(self):
        """앞쪽 데이터 제거 (주의: 리스트 특성상 O(N)이지만, 로직 구현을 위해 사용)"""
        if not self.is_empty():
            return self.items.pop(0)
            
    def back(self):
        """맨 뒤의 값 확인"""
        if not self.is_empty():
            return self.items[-1]
            
    def front(self):
        """맨 앞의 값 확인"""
        if not self.is_empty():
            return self.items[0]
            
    def is_empty(self):
        return len(self.items) == 0

# 메인 로직 시작
n, k = map(int, input().split())
A = list(map(int, input().split()))

dq = Deque() # 인덱스를 저장할 덱
B = []       # 결과 저장 리스트

for i in range(n):
    # 1. 덱의 뒤에서부터 현재 값(A[i])보다 큰 값들은 제거
    # (새로 들어온 값이 더 작다면, 기존의 큰 값들은 최솟값이 될 수 없음)
    while not dq.is_empty() and A[dq.back()] > A[i]:
        dq.pop_back()
    
    # 2. 현재 인덱스를 덱의 뒤에 추가
    dq.push_back(i)
    
    # 3. 윈도우 범위를 벗어난 인덱스는 덱의 앞에서 제거
    # (현재 인덱스 i에서 k만큼 이전인 i-k와 같거나 작으면 유효 범위 밖)
    if dq.front() <= i - k:
        dq.pop_front()
    
    # 4. 윈도우 크기가 k만큼 채워진 이후부터 결과 저장
    # 덱의 맨 앞(front)에 있는 인덱스가 현재 구간의 최솟값 위치임
    if i >= k - 1:
        B.append(A[dq.front()])

# 결과 출력
print(" ".join(map(str, B)))


# --- 주석 ---
# 사용 자료구조: 덱(Deque)을 클래스로 직접 구현하여 사용
#
# 알고리즘 설명:
#   '슬라이딩 윈도우'와 '모노톤 덱(Monotonic Deque)' 방식을 사용했습니다.
#   이중 반복문을 사용하여 매번 최솟값을 찾는 대신, 
#   덱에 '인덱스'를 저장하되, 연관된 값들이 항상 오름차순이 되도록 관리합니다.
#   1. 들어올 값보다 큰 값은 덱의 뒤에서 모두 제거 (pop_back)
#   2. 윈도우 범위를 벗어난 인덱스는 덱의 앞에서 제거 (pop_front)
#   이렇게 하면 덱의 맨 앞은 항상 현재 구간의 최솟값이 됩니다.
#
# 수행시간 분석:
#   각 원소는 덱에 한 번 들어가고(push), 최대 한 번 나옵니다(pop).
#   따라서 원소의 개수 N에 비례하는 선형 시간이 소요됩니다.
#   (참고: 파이썬 기본 리스트의 pop(0)은 느리지만, 알고리즘 논리 자체는 선형입니다.)
#