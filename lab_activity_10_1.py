# ============================================================
# Laboratory Activity 10 - Problem 1
# Student Name List Using Doubly Linked List
# ============================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Check if the list is empty
    def is_empty(self):
        return self.head is None

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.is_empty():
            self.head = new_node
            return

        # Find the last node
        current = self.head

        while current.next is not None:
            current = current.next

        # Connect the new node
        current.next = new_node
        new_node.prev = current

    # Display the list from first to last
    def display_forward(self):
        if self.is_empty():
            print("List is empty.")
            return

        print("Forward Display:")

        current = self.head

        print("HEAD → ", end="")

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" ⇄ ", end="")
            else:
                print(" → NULL")

            current = current.next

    # Display the list from last to first
    def display_backward(self):
        if self.is_empty():
            print("List is empty.")
            return

        # Find the last node
        current = self.head

        while current.next is not None:
            current = current.next

        print("Backward Display:")
        print("TAIL → ", end="")

        while current is not None:
            print(current.data, end="")

            if current.prev is not None:
                print(" ⇄ ", end="")
            else:
                print(" → NULL")

            current = current.prev


# ============================================================
# Main Program
# ============================================================

student_list = DoublyLinkedList()

number_of_students = int(input("Enter number of students: "))

for i in range(1, number_of_students + 1):
    name = input(f"Enter student name {i}: ")
    student_list.insert_at_end(name)

print()

student_list.display_forward()

print()

student_list.display_backward()


# ============================================================
# Guide Questions
# ============================================================

# 1. What is the purpose of the prev pointer?
# The prev pointer stores the address or reference of the previous node
# in the doubly linked list.

# 2. What is the purpose of the next pointer?
# The next pointer stores the address or reference of the next node
# in the doubly linked list.

# 3. Why can a doubly linked list be displayed backward?
# A doubly linked list can be displayed backward because every node
# contains a prev pointer that connects it to the previous node.

# 4. What is the difference between a singly linked list and a doubly
# linked list?
# A singly linked list has only a next pointer, while a doubly linked
# list has both prev and next pointers. Therefore, a doubly linked list
# can be traversed in both forward and backward directions.
