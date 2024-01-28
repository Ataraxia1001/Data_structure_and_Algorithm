#Node 정의
class Node:
    def __init__(self, data, next=None, back=None): # data 만 입력시 next 초기값은 None이다.
        self.data = data # 다음 데이터 주소 초기값 = None
        self.next = next # 앞에 있는 데이터를 가르킴(enqueue에 사용)
        self.back = back # 뒤에 있는 데이터를 가르킴(dequeue에 사용)
#     dequeue <- [1(head)->back, 2, <-next 3 back-> 4, <-next 5(tail)]  <- enqueue

class Queue:
    def __init__(self):
        # head와 tail 설정, 처음엔 값이 없음(None)
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # 노드 생성
        new_node = Node(data)
        new_node.next = self.tail # 새 데이터가 기존의 tail을 가르키게 함
        if self.tail == None:
            print('there was no data in queue')
        else:
            self.tail.back = new_node # 기존 tail이 새 데이터를 back으로 가르키게 함

        if self.head == None: # head가 없었을 경우(empty queue), 새로운 데이터가 head
            # new_node.next = self.head
            self.head = new_node
            print('there was no data in queue')

        self.tail = new_node # 이제 새로운 데이터가 tail(끝부분)

    def dequeue(self):
        if self.head == None:
            print('Empty queue')
        else: # there is head to dequeue
            data = self.head.data
            self.head = self.head.back
            print("dequeue():", data)

    def print_all(self):
        print("print queue")
        tracer = self.head
        if tracer == None:
            print("Empty queue")
        else:
            while (tracer != None):
                print(" ", tracer.data)
                tracer = tracer.back
        print("end")

def main():
    que = Queue()
    que.print_all()
    que.dequeue()
    que.enqueue(1)
    que.enqueue(2)
    que.print_all()
    que.dequeue()
    que.print_all()
    que.dequeue()
    que.print_all()

if __name__ == "__main__":
    main()


