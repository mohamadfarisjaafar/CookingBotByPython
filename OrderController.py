from collections import deque  # Importing deque for efficient order management
from Bot import Bot
from Order import Order

# Class to manage orders and bots
class OrderController:
    def __init__(self):
        self.orders = deque()  # Queue for normal orders
        self.vip_orders = deque()  # Queue for VIP orders
        self.complete_orders = []  # List to store completed orders
        self.bots = []  # List to store active bots
        self.order_counter = 0  # Counter to assign unique IDs to orders

    def create_order(self, is_vip=False):
        # Method to create a new order
        self.order_counter += 1  # Increment the order counter
        order = Order(self.order_counter, is_vip)  # Create a new order
        if is_vip:
            self.vip_orders.append(order)  # Add VIP order to the VIP queue
        else:
            self.orders.append(order)  # Add normal order to the normal queue
        print(f"New {'VIP' if is_vip else 'Normal'} order added: {order}")

    def create_bot(self):
        # Method to create a new bot
        bot_id = len(self.bots) + 1  # Assign a unique ID to the bot
        bot = Bot(bot_id)  # Create a new bot instance
        self.bots.append(bot)  # Add the bot to the list of bots
        # Start the bot in a new thread
        threading.Thread(target=bot.process_orders, args=(self,), daemon=True).start()
        print(f"Bot {bot_id} created and ready to process orders.")

    def remove_bot(self):
        # Method to remove an active bot
        if self.bots:
            bot = self.bots.pop()  # Remove the last added bot
            bot.stop()  # Stop the bot's thread
            print(f"Bot {bot.bot_id} has been stopped.")
        else:
            print("No bots to remove.")

    def get_next_order(self):
        # Get the next order for processing
        if self.vip_orders:  # Check VIP orders first
            return self.vip_orders.popleft()
        elif self.orders:  # If no VIP orders, check normal orders
            return self.orders.popleft()
        return None  # If no orders are available, return None

    def display_orders(self):
        # Display the current state of orders
        print("\n--- Order List ---")
        print("\nPending Orders:")
        for order in list(self.vip_orders) + list(self.orders):  # Combine VIP and normal orders
            print(order)

        print("\nComplete Orders:")
        for order in self.complete_orders:  # Display completed orders
            print(order)

    def display_bots(self):
        # Display the current state of bots
        print("\n--- Available Bots ---")
        for bot in self.bots:
            # Show whether a bot is idle or processing an order
            status = "Idle" if bot.current_order is None else f"Processing order {bot.current_order.order_id}"
            print(f"Bot {bot.bot_id}: {status}")
