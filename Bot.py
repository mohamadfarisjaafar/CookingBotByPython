# Class to represent a cooking bot
class Bot:
    def __init__(self, bot_id):
        self.bot_id = bot_id  # Unique ID for the bot
        self.current_order = None  # Initially, the bot is not processing any order
        self.active = True  # Flag to indicate if the bot is active

    def process_orders(self, controller):
        # Bot continuously checks for orders to process
        while self.active:
            if self.current_order is None:  # If the bot is idle
                order = controller.get_next_order()  # Get the next order from the controller
                if order:  # If an order is available
                    self.current_order = order  # Assign the order to the bot
                    print(f"Bot {self.bot_id} is processing order {order.order_id}...")
                    time.sleep(10)  # Simulate processing time of 1 second
                    order.status = "COMPLETE"  # Mark the order as complete
                    print(f"Bot {self.bot_id} completed order {order.order_id}")
                    controller.complete_orders.append(order)  # Move the order to the complete list
                    self.current_order = None  # Mark the bot as idle
                else:
                    time.sleep(0.5)  # If no orders, wait before checking again
            else:
                time.sleep(0.1)  # Small wait to prevent excessive CPU usage

    def stop(self):
        self.active = False  # Stop the bot gracefully

