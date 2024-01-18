#Node 정의
class Node:
    def __init__(self, data, next=None):  #data 만 입력시 next 초기값은 None이다.
        self.data = data #다음 데이터 주소 초기값 = None
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        # node 생성
        new_node = Node(data)
        # 새 node가 top 가르키게 함 (top 메모리 주소를 가르킴)
        # 즉, top이 기존에 가르키던 노드를 바라보게 함
        new_node.next = self.top
        # top 메모리 주소와 새 node의 메모리 주소가 같음
        self.top = new_node

    def pop(self):
        if self.top == None:
            print("Empty")
        else:
            data = self.top.data
            self.top = self.top.next
            print("pop():", data)
            
    def print_all(self):
        print("print stack")
        tracer = self.top
        if tracer == None:
            print("empty stack")
        else :
            while (tracer != None):
                print(" ", tracer.data)
                tracer = tracer.next
        print("end")


def main():
    st = Stack()
    st.print_all()
    st.pop()
    st.push(1)
    st.push(2)
    st.print_all()
    st.pop()
    st.print_all()
    st.pop()
    st.print_all()

if __name__ == "__main__":
    main()