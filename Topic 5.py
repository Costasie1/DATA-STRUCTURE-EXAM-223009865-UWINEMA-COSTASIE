class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, order_id, city, priority):
        if self.is_full():
            print("Queue is full. Cannot add more orders.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = {'order_id': order_id, 'city': city, 'priority': priority}

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No orders to process.")
            return None
        order = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return order

    def display_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        index = self.front
        while True:
            print(f"Order ID: {self.queue[index]['order_id']}, City: {self.queue[index]['city']}, Priority: {self.queue[index]['priority']}")
            if index == self.rear:
                break
            index = (index + 1) % self.max_size

orders = CircularQueue(max_size=5)
orders.enqueue(1, "City A", 3)
orders.enqueue(2, "City B", 1)
orders.enqueue(3, "City C", 2)
orders.enqueue(4, "City D", 4)
orders.enqueue(5, "City E", 1)
orders.enqueue(6, "City F", 2) 
print("Orders in the queue:")
orders.display_queue()

print("\nProcessing orders:")
while not orders.is_empty():
    order = orders.dequeue()
    print(f"Processed Order ID: {order['order_id']}, City: {order['city']}, Priority: {order['priority']}")
