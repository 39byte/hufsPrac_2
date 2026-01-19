class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # [최적화] 끝 부분 접근을 O(1)로 하기 위해 tail 추가
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def printList(self): # 변경없이 사용할 것!
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")
    
    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        
        # [최적화] 리스트가 비어있었다면 tail도 head와 같음
        if self.size == 0:
            self.tail = new_node
            
        self.size += 1
        return new_node

    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # [최적화] 순회(loop) 없이 tail을 이용해 O(1)로 추가
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1
        return new_node

    def popFront(self): 
        if self.size == 0:
            return None
        
        x = self.head
        self.head = self.head.next
        self.size -= 1
        
        # [최적화] 노드가 하나였는데 삭제해서 0이 된 경우 tail도 초기화
        if self.size == 0:
            self.tail = None
            
        return x
            
    def popBack(self):
        if self.size == 0:
            return None
        
        # [버그 수정] 노드가 1개일 때 처리가 제대로 안되던 문제 해결
        if self.size == 1:
            x = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return x
        
        # Singly Linked List라서 tail 삭제 시 바로 이전 노드를 찾기 위해 순회 필요 O(n)
        prev = self.head
        while prev.next != self.tail:
            prev = prev.next
        
        x = self.tail
        prev.next = None
        self.tail = prev # tail 포인터 갱신
        self.size -= 1

        return x

    def search(self, key):
        now_node = self.head
        while now_node is not None:
            if now_node.key == key:
                return now_node
            now_node = now_node.next
        return None

    def remove(self, x):
        # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
        if self.size == 0 or x is None:
            return False

        # [버그 수정] 삭제하려는 노드가 head인 경우 처리
        if self.head == x:
            self.popFront() # 이미 구현된 popFront 활용 (size, tail 처리 포함됨)
            return True

        # head가 아닌 경우 탐색
        prev = self.head
        while prev.next is not None:
            if prev.next == x:
                prev.next = x.next
                
                # [버그 수정] 삭제된 노드가 tail이었다면 tail 갱신
                if x == self.tail:
                    self.tail = prev
                
                self.size -= 1
                return True
            prev = prev.next
            
        return False
                
    def size(self): # 메서드 이름 충돌 방지 (하지만 문제 요구사항 유지)
        return self.size
    
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back.")
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):
            print(x.key, "is removed.")
        else:
            print("Key is not removed for some reason.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")