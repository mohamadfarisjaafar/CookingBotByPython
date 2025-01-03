from collections import deque

# Class to represent an order
class Order:
    def __init__(self, order_id, is_vip=False):
        self.order_id = order_id  # Unique ID for the order
        self.is_vip = is_vip  # Flag to identify if the order is a VIP order
        self.status = "PENDING"  # Initial status of the order is PENDING

    def __repr__(self):
        # String representation of an order
        return f"Order({self.order_id}, {'VIP' if self.is_vip else 'Normal'}, {self.status})"

