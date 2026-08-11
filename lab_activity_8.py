# ============================================================
# Laboratory Activity 8
# Sorted Linked List with Menu
# Student Number Sorted Linked List System
# ============================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # --------------------------------------------------------
    # Check if the linked list is empty
    # --------------------------------------------------------
    def is_empty(self):
        return self.head is None

    # --------------------------------------------------------
    # Insert a student number in sorted order
    # --------------------------------------------------------
    def insert_sorted(self, data):
        new_node = Node(data)

        # Case 1: List is empty
        if self.is_empty():
            self.head = new_node

        # Case 2: Insert before the current head
        elif data < self.head.data:
            new_node.next = self.head
            self.head = new_node

        # Case 3: Insert in the middle or at the end
        else:
            current = self.head

            while current.next is not None and current.next.data < data:
                current = current.next

            new_node.next = current.next
            current.next = new_node

        print(f"{data} inserted successfully.")

    # --------------------------------------------------------
    # Delete the first node
    # --------------------------------------------------------
    def delete_front(self):
        if self.is_empty():
            print("Linked list is empty. Cannot delete from front.")
            return

        deleted_value = self.head.data

        self.head = self.head.next

        print(f"{deleted_value} deleted from the front successfully.")

    # --------------------------------------------------------
    # Delete the last node
    # --------------------------------------------------------
    def delete_end(self):
        if self.is_empty():
            print("Linked list is empty. Cannot delete from end.")
            return

        # If there is only one node
        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None

            print(f"{deleted_value} deleted from the end successfully.")
            return

        # Find the second-to-the-last node
        current = self.head

        while current.next.next is not None:
            current = current.next

        deleted_value = current.next.data

        current.next = None

        print(f"{deleted_value} deleted from the end successfully.")

    # --------------------------------------------------------
    # Delete a node by value
    # --------------------------------------------------------
    def delete_by_value(self, data):
        if self.is_empty():
            print("Linked list is empty.")
            return

        # If the value is found at the head
        if self.head.data == data:
            self.head = self.head.next

            print(f"{data} deleted successfully.")
            return

        current = self.head

        # Since the list is sorted, stop when values become too large
        while current.next is not None and current.next.data < data:
            current = current.next

        if current.next is not None and current.next.data == data:
            current.next = current.next.next

            print(f"{data} deleted successfully.")
        else:
            print(f"{data} not found in the linked list.")

    # --------------------------------------------------------
    # Search for a student number
    # --------------------------------------------------------
    def search(self, data):
        current = self.head

        while current is not None:

            if current.data == data:
                print(f"{data} found in the linked list.")
                return True

            # Stop early because the list is sorted
            if current.data > data:
                break

            current = current.next

        print(f"{data} not found in the linked list.")
        return False

    # --------------------------------------------------------
    # Display the linked list
    # --------------------------------------------------------
    def display(self):
        if self.is_empty():
            print("Linked list is empty.")
            return

        print("Linked List:")
        print("HEAD → ", end="")

        current = self.head

        while current is not None:
            print(f"[{current.data}] → ", end="")
            current = current.next

        print("NULL")

    # --------------------------------------------------------
    # Clear the entire linked list
    # --------------------------------------------------------
    def clear(self):
        self.head = None

        print("Linked list has been cleared.")


# ============================================================
# Main Program
# ============================================================

student_list = LinkedList()


while True:

    print()
    print("========================================")
    print("STUDENT NUMBER SORTED LINKED LIST SYSTEM")
    print("========================================")
    print("[1] Insert Student Number")
    print("[2] Delete Front")
    print("[3] Delete End")
    print("[4] Delete by Value")
    print("[5] Search Student Number")
    print("[6] Display Linked List")
    print("[7] Check if Empty")
    print("[8] Clear Linked List")
    print("[9] Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    # --------------------------------------------------------
    # Insert Student Number
    # --------------------------------------------------------
    if choice == "1":

        try:
            student_number = int(
                input("Enter student number to insert: ")
            )

            student_list.insert_sorted(student_number)

        except ValueError:
            print("Invalid input. Please enter an integer.")

    # --------------------------------------------------------
    # Delete Front
    # --------------------------------------------------------
    elif choice == "2":

        student_list.delete_front()

    # --------------------------------------------------------
    # Delete End
    # --------------------------------------------------------
    elif choice == "3":

        student_list.delete_end()

    # --------------------------------------------------------
    # Delete by Value
    # --------------------------------------------------------
    elif choice == "4":

        try:
            student_number = int(
                input("Enter student number to delete: ")
            )

            student_list.delete_by_value(student_number)

        except ValueError:
            print("Invalid input. Please enter an integer.")

    # --------------------------------------------------------
    # Search Student Number
    # --------------------------------------------------------
    elif choice == "5":

        try:
            student_number = int(
                input("Enter student number to search: ")
            )

            student_list.search(student_number)

        except ValueError:
            print("Invalid input. Please enter an integer.")

    # --------------------------------------------------------
    # Display Linked List
    # --------------------------------------------------------
    elif choice == "6":

        student_list.display()

    # --------------------------------------------------------
    # Check if Empty
    # --------------------------------------------------------
    elif choice == "7":

        if student_list.is_empty():
            print("Linked list is empty.")
        else:
            print("Linked list is not empty.")

    # --------------------------------------------------------
    # Clear Linked List
    # --------------------------------------------------------
    elif choice == "8":

        student_list.clear()

    # --------------------------------------------------------
    # Exit
    # --------------------------------------------------------
    elif choice == "9":

        print("Program terminated.")
        break

    # --------------------------------------------------------
    # Invalid Menu Choice
    # --------------------------------------------------------
    else:

        print("Invalid choice. Please enter 1 to 9.")


# ============================================================
# Guide Questions
# ============================================================

# 1. What is a sorted linked list?
# A sorted linked list is a linked list in which the values are
# automatically arranged in a specific order, such as ascending order.

# 2. What is the purpose of the head pointer in a linked list?
# The head pointer stores the reference to the first node of the
# linked list.

# 3. Why does insert_sorted() need to compare values?
# It compares values to determine the correct position where the
# new node should be inserted while maintaining sorted order.

# 4. What happens when the new value is smaller than the head value?
# The new node is inserted before the current head and becomes
# the new head of the linked list.

# 5. What happens when the new value is greater than all existing values?
# The new node is inserted at the end of the linked list.

# 6. What is the difference between insert_at_end() and insert_sorted()?
# insert_at_end() always adds the new node at the end, while
# insert_sorted() places the new node in its correct sorted position.

# 7. Why is traversal needed when inserting a value in sorted order?
# Traversal is needed to find the correct position where the new node
# should be inserted.

# 8. What happens when delete_front() is performed?
# The first node is removed and the head pointer is moved to the
# second node.

# 9. What happens when delete_end() is performed?
# The last node is removed and the next pointer of the
# second-to-the-last node becomes None.

# 10. Why should links be updated carefully when deleting a node?
# Links must be updated correctly to keep the remaining nodes
# connected and prevent the linked list from becoming broken.
