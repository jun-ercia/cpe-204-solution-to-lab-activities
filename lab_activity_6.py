# ============================================================
# Program Title : Customer Service Queue Management System
# Purpose       : This program manages customers using Queue
#                 ADT implemented with a linked list.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Your Name
# ============================================================


# ------------------------------------------------------------
# Class: Node
# Purpose: Represents one element in the linked list queue.
# ------------------------------------------------------------
class Node:

    def __init__(self, data):
        # Store the value of the node
        self.data = data

        # Reference to the next node
        self.next = None


# ------------------------------------------------------------
# Class: LinkedQueue
# Purpose: Implements Queue ADT using a linked list.
# ------------------------------------------------------------
class LinkedQueue:

    def __init__(self):
        # FRONT points to the first node
        self.FRONT = None

        # REAR points to the last node
        self.REAR = None

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks whether the queue has no nodes.
    # --------------------------------------------------------
    def is_empty(self):
        return self.FRONT is None

    # --------------------------------------------------------
    # Method: enqueue
    # Purpose: Adds a new node at the rear of the queue.
    # --------------------------------------------------------
    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.FRONT = new_node
            self.REAR = new_node
        else:
            self.REAR.next = new_node
            self.REAR = new_node

    # --------------------------------------------------------
    # Method: dequeue
    # Purpose: Removes and returns the front element.
    # --------------------------------------------------------
    def dequeue(self):
        if self.is_empty():
            return None

        temp = self.FRONT
        item = temp.data

        self.FRONT = self.FRONT.next

        if self.FRONT is None:
            self.REAR = None

        temp.next = None

        return item

    # --------------------------------------------------------
    # Method: peek
    # Purpose: Returns the front element without removing it.
    # --------------------------------------------------------
    def peek(self):
        if self.is_empty():
            return None

        return self.FRONT.data

    # --------------------------------------------------------
    # Method: size
    # Purpose: Counts and returns the number of nodes.
    # --------------------------------------------------------
    def size(self):
        count = 0
        current = self.FRONT

        while current is not None:
            count += 1
            current = current.next

        return count

    # --------------------------------------------------------
    # Method: search
    # Purpose: Searches for a customer using customer number.
    # Returns the customer record and position if found.
    # --------------------------------------------------------
    def search(self, customer_number):
        current = self.FRONT
        position = 1

        while current is not None:
            if current.data["customer_number"] == customer_number:
                return current.data, position

            current = current.next
            position += 1

        return None, -1

    # --------------------------------------------------------
    # Method: display
    # Purpose: Displays customers from FRONT to REAR.
    # --------------------------------------------------------
    def display(self):
        if self.is_empty():
            print("No customers in the queue.")
            return

        print("\nCUSTOMERS IN QUEUE")
        print("--------------------------------------------------")

        current = self.FRONT
        position = 1

        while current is not None:
            customer = current.data

            print("Position:", position)
            print("Customer Number:", customer["customer_number"])
            print("Customer Name:", customer["customer_name"])
            print("Service Needed:", customer["service_needed"])
            print("--------------------------------------------------")

            current = current.next
            position += 1

    # --------------------------------------------------------
    # Method: display_structure
    # Purpose: Displays the linked-list queue structure.
    # --------------------------------------------------------
    def display_structure(self):
        if self.is_empty():
            print("FRONT = None")
            print("REAR  = None")
            print("Queue is empty.")
            return

        print("\nLinked List Queue Structure:")
        print("FRONT")

        current = self.FRONT

        while current is not None:
            customer = current.data

            print("  ↓")
            print("[", customer["customer_number"], " | ",
                  customer["customer_name"], " | ",
                  customer["service_needed"], " | NEXT ]", sep="")

            current = current.next

        print("  ↓")
        print("NULL")
        print("REAR points to:", self.REAR.data["customer_number"])

    # --------------------------------------------------------
    # Method: clear
    # Purpose: Removes all nodes from the queue.
    # --------------------------------------------------------
    def clear(self):
        current = self.FRONT

        while current is not None:
            next_node = current.next
            current.next = None
            current = next_node

        self.FRONT = None
        self.REAR = None


# ------------------------------------------------------------
# Function: get_non_blank_input
# Purpose : Prevents blank input.
# ------------------------------------------------------------
def get_non_blank_input(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("Customer information cannot be blank.")


# ------------------------------------------------------------
# Function: display_customer
# Purpose : Displays one customer record.
# ------------------------------------------------------------
def display_customer(customer):
    print("Customer Number:", customer["customer_number"])
    print("Customer Name:", customer["customer_name"])
    print("Service Needed:", customer["service_needed"])


# ------------------------------------------------------------
# Function: display_menu
# Purpose : Displays the main menu.
# ------------------------------------------------------------
def display_menu():
    print("\n==================================================")
    print("CUSTOMER SERVICE QUEUE MANAGEMENT SYSTEM")
    print("Queue ADT Using Linked List")
    print("==================================================")
    print("[1] Add Customer to Queue")
    print("[2] Serve Next Customer")
    print("[3] View Next Customer")
    print("[4] Search for a Customer")
    print("[5] Display All Customers")
    print("[6] Check if Queue is Empty")
    print("[7] Display Number of Customers")
    print("[8] Clear Customer Queue")
    print("[9] Display Linked List Queue Structure")
    print("[10] Exit")
    print("==================================================")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
customer_queue = LinkedQueue()

try:
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        # ----------------------------------------------------
        # Option 1: Add Customer to Queue
        # ----------------------------------------------------
        if choice == 1:
            customer_number = get_non_blank_input("Enter customer number: ")

            existing_customer, position = customer_queue.search(customer_number)

            if existing_customer is not None:
                print("Customer number already exists.")
            else:
                customer_name = get_non_blank_input("Enter customer name: ")
                service_needed = get_non_blank_input("Enter service needed: ")

                customer_record = {
                    "customer_number": customer_number,
                    "customer_name": customer_name,
                    "service_needed": service_needed
                }

                customer_queue.enqueue(customer_record)

                print("Customer added to the queue successfully.")

        # ----------------------------------------------------
        # Option 2: Serve Next Customer
        # ----------------------------------------------------
        elif choice == 2:
            customer = customer_queue.dequeue()

            if customer is None:
                print("No customer available to serve.")
            else:
                print("Customer served successfully.")
                display_customer(customer)

        # ----------------------------------------------------
        # Option 3: View Next Customer
        # ----------------------------------------------------
        elif choice == 3:
            customer = customer_queue.peek()

            if customer is None:
                print("No next customer available.")
            else:
                print("Next Customer:")
                display_customer(customer)

        # ----------------------------------------------------
        # Option 4: Search for a Customer
        # ----------------------------------------------------
        elif choice == 4:
            customer_number = get_non_blank_input("Enter customer number to search: ")

            customer, position = customer_queue.search(customer_number)

            if customer is None:
                print("Customer not found.")
            else:
                print("Customer Found:")
                display_customer(customer)
                print("Position in Queue:", position)

        # ----------------------------------------------------
        # Option 5: Display All Customers
        # ----------------------------------------------------
        elif choice == 5:
            customer_queue.display()

        # ----------------------------------------------------
        # Option 6: Check if Queue is Empty
        # ----------------------------------------------------
        elif choice == 6:
            if customer_queue.is_empty():
                print("The customer queue is empty.")
            else:
                print("The customer queue is not empty.")

        # ----------------------------------------------------
        # Option 7: Display Number of Customers
        # ----------------------------------------------------
        elif choice == 7:
            print("Number of customers in the queue:", customer_queue.size())

        # ----------------------------------------------------
        # Option 8: Clear Customer Queue
        # ----------------------------------------------------
        elif choice == 8:
            if customer_queue.is_empty():
                print("The customer queue is already empty.")
            else:
                customer_queue.clear()
                print("The customer queue has been cleared.")

        # ----------------------------------------------------
        # Option 9: Display Linked List Queue Structure
        # ----------------------------------------------------
        elif choice == 9:
            customer_queue.display_structure()

        # ----------------------------------------------------
        # Option 10: Exit Program
        # ----------------------------------------------------
        elif choice == 10:
            print("Program ended. Thank you!")
            break

        # ----------------------------------------------------
        # Invalid Menu Number
        # ----------------------------------------------------
        else:
            print("Invalid menu choice. Please enter a number from 1 to 10.")

except KeyboardInterrupt:
    print("\nProgram stopped by the user.")

except EOFError:
    print("\nInput ended unexpectedly.")

except Exception as error:
    print("An unexpected error occurred:", error)
