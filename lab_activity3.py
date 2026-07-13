# ============================================================
# Program Title : Task Management System Using Singly Linked List
# Purpose       : This program manages tasks using a singly
#                 linked list. It allows the user to add, delete,
#                 search, display, complete, clear, and check tasks.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Your Name
# ============================================================


# ------------------------------------------------------------
# Class: Node
# Purpose: Represents one node in the linked list.
# Each node contains a task record and a pointer to the next node.
# ------------------------------------------------------------
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# ------------------------------------------------------------
# Class: SinglyLinkedList
# Purpose: Represents the linked list and its operations.
# ------------------------------------------------------------
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # --------------------------------------------------------
    # Method: make_null
    # Purpose: Clears the linked list.
    # --------------------------------------------------------
    def make_null(self):
        self.head = None

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the linked list has no nodes.
    # --------------------------------------------------------
    def is_empty(self):
        return self.head is None

    # --------------------------------------------------------
    # Method: insert_at_end
    # Purpose: Inserts a new task record at the end of the list.
    # --------------------------------------------------------
    def insert_at_end(self, task_record):
        new_node = Node(task_record)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # --------------------------------------------------------
    # Method: delete_by_value
    # Purpose: Deletes a task using Task ID.
    # --------------------------------------------------------
    def delete_by_value(self, task_id):
        if self.head is None:
            return False

        if self.head.data["task_id"] == task_id:
            self.head = self.head.next
            return True

        prev = self.head
        curr = self.head.next

        while curr is not None and curr.data["task_id"] != task_id:
            prev = curr
            curr = curr.next

        if curr is None:
            return False

        prev.next = curr.next
        return True

    # --------------------------------------------------------
    # Method: search
    # Purpose: Searches for a task using Task ID.
    # --------------------------------------------------------
    def search(self, task_id):
        temp = self.head

        while temp is not None:
            if temp.data["task_id"] == task_id:
                return temp.data

            temp = temp.next

        return None

    # --------------------------------------------------------
    # Method: traverse
    # Purpose: Displays all task records.
    # --------------------------------------------------------
    def traverse(self):
        if self.head is None:
            print("No tasks available.")
            return

        temp = self.head

        print("\nTask List:\n")

        while temp is not None:
            task = temp.data

            print("Task ID:", task["task_id"])
            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Priority:", task["priority"])
            print("Status:", task["status"])
            print()

            temp = temp.next

    # --------------------------------------------------------
    # Method: mark_completed
    # Purpose: Updates the status of a task to Completed.
    # --------------------------------------------------------
    def mark_completed(self, task_id):
        temp = self.head

        while temp is not None:
            if temp.data["task_id"] == task_id:
                temp.data["status"] = "Completed"
                return True

            temp = temp.next

        return False


# ------------------------------------------------------------
# Function: get_non_blank_input
# Purpose: Prevents blank input from the user.
# ------------------------------------------------------------
def get_non_blank_input(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("Input cannot be blank. Please try again.")


# ------------------------------------------------------------
# Function: display_task
# Purpose: Displays one task record.
# ------------------------------------------------------------
def display_task(task):
    print("\nTask Found:")
    print("Task ID:", task["task_id"])
    print("Title:", task["title"])
    print("Description:", task["description"])
    print("Priority:", task["priority"])
    print("Status:", task["status"])


# ------------------------------------------------------------
# Function: display_menu
# Purpose: Displays the main menu.
# ------------------------------------------------------------
def display_menu():
    print("\n========================================")
    print("TASK MANAGEMENT SYSTEM")
    print("Using Singly Linked List")
    print("========================================")
    print("[1] Add Task")
    print("[2] Delete Task")
    print("[3] Search Task")
    print("[4] Display All Tasks")
    print("[5] Mark Task as Completed")
    print("[6] Check if List is Empty")
    print("[7] Clear All Tasks")
    print("[8] Exit")
    print("========================================")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
task_list = SinglyLinkedList()

while True:
    display_menu()

    choice = input("Enter your choice: ").strip()

    # --------------------------------------------------------
    # Option 1: Add Task
    # --------------------------------------------------------
    if choice == "1":
        task_id = get_non_blank_input("Enter Task ID: ")

        # Check for duplicate Task ID
        if task_list.search(task_id) is not None:
            print("Task ID already exists.")
        else:
            title = get_non_blank_input("Enter Task Title: ")
            description = get_non_blank_input("Enter Task Description: ")
            priority = get_non_blank_input("Enter Priority Level: ")
            status = get_non_blank_input("Enter Status: ")

            task_record = {
                "task_id": task_id,
                "title": title,
                "description": description,
                "priority": priority,
                "status": status
            }

            task_list.insert_at_end(task_record)
            print("Task added successfully.")

    # --------------------------------------------------------
    # Option 2: Delete Task
    # --------------------------------------------------------
    elif choice == "2":
        task_id = get_non_blank_input("Enter Task ID to delete: ")

        if task_list.delete_by_value(task_id):
            print("Task deleted successfully.")
        else:
            print("Task not found.")

    # --------------------------------------------------------
    # Option 3: Search Task
    # --------------------------------------------------------
    elif choice == "3":
        task_id = get_non_blank_input("Enter Task ID to search: ")

        task = task_list.search(task_id)

        if task is not None:
            display_task(task)
        else:
            print("Task not found.")

    # --------------------------------------------------------
    # Option 4: Display All Tasks
    # --------------------------------------------------------
    elif choice == "4":
        task_list.traverse()

    # --------------------------------------------------------
    # Option 5: Mark Task as Completed
    # --------------------------------------------------------
    elif choice == "5":
        task_id = get_non_blank_input("Enter Task ID to mark as completed: ")

        if task_list.mark_completed(task_id):
            print("Task marked as completed.")
        else:
            print("Task not found.")

    # --------------------------------------------------------
    # Option 6: Check if List is Empty
    # --------------------------------------------------------
    elif choice == "6":
        if task_list.is_empty():
            print("The task list is empty.")
        else:
            print("The task list is not empty.")

    # --------------------------------------------------------
    # Option 7: Clear All Tasks
    # --------------------------------------------------------
    elif choice == "7":
        task_list.make_null()
        print("All tasks have been cleared.")

    # --------------------------------------------------------
    # Option 8: Exit Program
    # --------------------------------------------------------
    elif choice == "8":
        print("Program ended. Thank you!")
        break

    # --------------------------------------------------------
    # Invalid Menu Choice
    # --------------------------------------------------------
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
