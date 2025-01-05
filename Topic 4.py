class Node:
    def __init__(self, order_id, city, priority):
        self.order_id = order_id
        self.city = city
        self.priority = priority
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def add_order(self, order_id, city, priority):
        new_node = Node(order_id, city, priority)
        if self.size == self.max_size:
            self.remove_order()
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def remove_order(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.size -= 1

    def display_orders(self):
        current = self.head
        while current is not None:
            print(f"Order ID: {current.order_id}, City: {current.city}, Priority: {current.priority}")
            current = current.next

orders = DoublyLinkedList(max_size=5)
orders.add_order(1, "City A", 3)
orders.add_order(2, "City B", 1)
orders.add_order(3, "City C", 2)
orders.add_order(4, "City D", 4)
orders.add_order(5, "City E", 1)
orders.add_order(6, "City F", 2) 
orders.display_orders()
