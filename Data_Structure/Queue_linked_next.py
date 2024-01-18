#Node 정의
class Node:
    def __init__(self, data, next=None): # data 만 입력시 next 초기값은 None이다.
        self.data = data # 다음 데이터 주소 초기값 = None
        self.next = next 
      
#     dequeue <- [1(head), 2, <-next 3, 4, <-next 5(tail)]  <- enqueue

class Queue:
    def __init__(self):
        # head와 tail 설정, 처음엔 값이 없음(None)
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # 노드 생성
        new_node = Node(data)
   
        if self.tail == None:
            print('there was no data in queue')
        else:
            self.tail.next = new_node # 기존 tail이 새 데이터를 가르키게 함

        if self.head == None: # head가 없었을 경우(empty queue), 새로운 데이터가 head
            self.head = new_node
            print('there was no data in queue')

        self.tail = new_node # 이제 새로운 데이터가 tail(끝부분)
        print('data was added')

    def dequeue(self):
        if self.head == None:
            print('Empty queue')
        else: # there is head to dequeue
            data = self.head.data
            self.head = self.head.next
            print("dequeue():", data)

    def print_all(self):
        print("print queue")
        tracer = self.head
        if tracer == None:
            print("Empty queue")
        else:
            while (tracer != None):
                print(" ", tracer.data)
                tracer = tracer.next
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


