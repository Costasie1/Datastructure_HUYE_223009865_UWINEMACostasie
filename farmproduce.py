from collections import deque

class FarmProduceDeliverySystem:
    def __init__(self):
        self.available_produce = [] 
        self.pending_deliveries = deque() 
        self.undo_stack = []  

    def add_produce(self, produce):
        self.available_produce.append(produce)
        print(f"Added produce: {produce}")
    def remove_produce(self, produce):
        if produce in self.available_produce:
            self.available_produce.remove(produce)
            print(f"Removed produce: {produce}")
        else:
            print(f"Produce {produce} not found")

    def add_delivery(self, delivery):
        self.pending_deliveries.append(delivery)
        print(f"Added delivery: {delivery}")

    def process_delivery(self):
        if self.pending_deliveries:
            delivery = self.pending_deliveries.popleft()
            self.undo_stack.append(delivery)
            print(f"Processed delivery: {delivery}")
        else:
            print("No pending deliveries")

    def undo_last_delivery(self):
        if self.undo_stack:
            last_delivery = self.undo_stack.pop()
            self.pending_deliveries.appendleft(last_delivery)
            print(f"Undid delivery: {last_delivery}")
        else:
            print("No deliveries to undo")


farm_system = FarmProduceDeliverySystem()
farm_system.add_produce("rice")
farm_system.add_produce("yams")
farm_system.add_delivery("rice")
farm_system.add_delivery("yams")
farm_system.process_delivery()
farm_system.undo_last_delivery()