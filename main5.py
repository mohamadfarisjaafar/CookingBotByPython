import time  # Importing time module for simulating order processing
from collections import deque  # Importing deque for efficient order management
import threading  # Importing threading for managing bots in parallel
from OrderController import OrderController

def run_cli():
    # CLI interface for the application
    controller = OrderController()

    while True:
        # Display menu options
        print("\nSelect an option:")
        print("1. New Normal Order")
        print("2. New VIP Order")
        print("3. + Bot (Add a bot)")
        print("4. - Bot (Remove a bot)")
        print("5. Show Orders")
        print("6. Show Available Bots")
        print("7. Exit")

        # Get user input
        choice = input("Enter your choice: ")

        if choice == '1':
            controller.create_order(is_vip=False)  # Create a normal order
        elif choice == '2':
            controller.create_order(is_vip=True)  # Create a VIP order
        elif choice == '3':
            controller.create_bot()  # Add a bot
        elif choice == '4':
            controller.remove_bot()  # Remove a bot
        elif choice == '5':
            controller.display_orders()  # Display orders
        elif choice == '6':
            controller.display_bots()  # Display bots
        elif choice == '7':
            print("Exiting the application.")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


if __name__ == "__main__":
    # Entry point of the program
    run_cli()
