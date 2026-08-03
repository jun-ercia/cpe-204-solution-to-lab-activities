# ============================================================
# Laboratory Activity 9 - Problem 1
# Title   : Display a Linked List in Reverse Order
# Name    : ______________________________
# Section : ______________________________
# ============================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current = self.head
        print("HEAD", end="")

        while current is not None:
            print(f" → {current.data}", end="")
            current = current.next

        print(" → NULL")

    def display_reverse_helper(self, node):
        if node is None:
            return

        self.display_reverse_helper(node.next)
        print(node.data, end="")

        if node != self.head:
            print(" → ", end="")

    def display_reverse(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        self.display_reverse_helper(self.head)
        print()


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    linked_list = LinkedList()

    number_of_values = get_positive_integer("Enter number of values: ")

    for i in range(1, number_of_values + 1):
        value = get_positive_integer(f"Enter value {i}: ")
        linked_list.insert_at_end(value)

    print("\nOriginal Linked List:")
    linked_list.display()

    print("\nLinked List in Reverse Order:")
    linked_list.display_reverse()


main()


# Guide Questions:
# 1. Why does a singly linked list normally move only in one direction?
#    A singly linked list normally moves only in one direction because each node
#    only has a next pointer that points to the next node.
#
# 2. Why is displaying a linked list in reverse order more difficult than displaying it normally?
#    It is more difficult because a singly linked list does not have a previous pointer.
#    The list can only be traversed from head to the next node.
#
# 3. What technique did you use to display the list in reverse order?
#    I used recursion. The function first goes to the last node, then displays the
#    data while returning from the recursive calls.
