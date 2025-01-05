import heapq

class Order:
    def __init__(self, order_id, city, priority):
        self.order_id = order_id
        self.city = city
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class WasteManagementHeap:
    def __init__(self):
        self.heap = []

    def add_order(self, order_id, city, priority):
        order = Order(order_id, city, priority)
        heapq.heappush(self.heap, order)

    def process_order(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

    def display_orders(self):
        for order in self.heap:
            print(f"Order ID: {order.order_id}, City: {order.city}, Priority: {order.priority}")

# Example usage
wm_heap = WasteManagementHeap()
wm_heap.add_order(1, "City A", 3)
wm_heap.add_order(2, "City B", 1)
wm_heap.add_order(3, "City C", 2)
wm_heap.add_order(4, "City D", 4)
wm_heap.add_order(5, "City E", 1)

print("Orders in the heap:")
wm_heap.display_orders()

print("\nProcessing orders:")
while wm_heap.heap:
    order = wm_heap.process_order()
    print(f"Processed Order ID: {order.order_id}, City: {order.city}, Priority: {order.priority}")
