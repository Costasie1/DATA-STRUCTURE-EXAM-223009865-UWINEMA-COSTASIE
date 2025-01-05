class AVLNode:
    def __init__(self, order_id, city, priority):
        self.order_id = order_id
        self.city = city
        self.priority = priority
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, order_id, city, priority):
        if not root:
            return AVLNode(order_id, city, priority)
        elif priority < root.priority:
            root.left = self.insert(root.left, order_id, city, priority)
        else:
            root.right = self.insert(root.right, order_id, city, priority)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and priority < root.left.priority:
            return self.right_rotate(root)
        if balance < -1 and priority > root.right.priority:
            return self.left_rotate(root)
        if balance > 1 and priority > root.left.priority:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and priority < root.right.priority:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        print(f"Order ID: {root.order_id}, City: {root.city}, Priority: {root.priority}")
        self.pre_order(root.left)
        self.pre_order(root.right)
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
# AVL Tree Example
avl_tree = AVLTree()
root = None
root = avl_tree.insert(root, 1, "City A", 3)
root = avl_tree.insert(root, 2, "City B", 1)
root = avl_tree.insert(root, 3, "City C", 2)
root = avl_tree.insert(root, 4, "City D", 4)
root = avl_tree.insert(root, 5, "City E", 1)

print("AVL Tree (Pre-Order Traversal):")
avl_tree.pre_order(root)

# Circular Queue Example
orders = CircularQueue(max_size=5)
orders.enqueue(1, "City A", 3)
orders.enqueue(2, "City B", 1)
orders.enqueue(3, "City C", 2)
orders.enqueue(4, "City D", 4)
orders.enqueue(5, "City E", 1)
orders.enqueue(6, "City F", 2)  # This will not be added as the queue is full

print("\nCircular Queue:")
orders.display_queue()

print("\nProcessing orders from Circular Queue:")
while not orders.is_empty():
    order = orders.dequeue()
    print(f"Processed Order ID: {order['order_id']}, City: {order['city']}, Priority: {order['priority']}")
