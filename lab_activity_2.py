# ============================================================
# Program Title : Student Record Management Using Singly Linked List
# Purpose       : This program manages student records using a
#                 singly linked list. It allows the user to add,
#                 delete, search, display, clear, and check student
#                 records.
# Date Written  : July 1, 2026
# Language      : Python 3
# Written by    : Jun Ercia
# ============================================================


# ------------------------------------------------------------
# Class: Node
# Purpose: Represents one node in the linked list.
# Each node stores one student record and a pointer to the next node.
# ------------------------------------------------------------
class Node:

    def __init__(self, data):
        # Store the student record in the node
        self.data = data

        # Store the reference to the next node
        self.next = None


# ------------------------------------------------------------
# Class: SinglyLinkedList
# Purpose: Represents the linked list and its operations.
# ------------------------------------------------------------
class SinglyLinkedList:

    def __init__(self):
        # The head points to the first node of the linked list
        self.head = None

    # --------------------------------------------------------
    # Method: make_null
    # Purpose: Clears the linked list by setting head to None.
    # --------------------------------------------------------
    def make_null(self):
        self.head = None

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the linked list has no records.
    # --------------------------------------------------------
    def is_empty(self):
        return self.head is None

    # --------------------------------------------------------
    # Method: insert_at_end
    # Purpose: Inserts a new student record at the end of the list.
    # --------------------------------------------------------
    def insert_at_end(self, student_record):
        new_node = Node(student_record)

        # If the list is empty, the new node becomes the first node
        if self.head is None:
            self.head = new_node
            return

        # Move to the last node
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        # Attach the new node after the last node
        temp.next = new_node

    # --------------------------------------------------------
    # Method: delete_by_value
    # Purpose: Deletes a student record using Student ID.
    # --------------------------------------------------------
    def delete_by_value(self, student_id):
        # If the list is empty, there is nothing to delete
        if self.head is None:
            return False

        # Check if the student record is found at the first node
        if self.head.data["student_id"] == student_id:
            self.head = self.head.next
            return True

        # Use two pointers to search for the record
        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data["student_id"] == student_id:
                prev.next = curr.next
                return True

            prev = curr
            curr = curr.next

        return False

    # --------------------------------------------------------
    # Method: search
    # Purpose: Searches for a student record using Student ID.
    # --------------------------------------------------------
    def search(self, student_id):
        temp = self.head

        # Visit each node until the student ID is found
        while temp is not None:
            if temp.data["student_id"] == student_id:
                return temp.data

            temp = temp.next

        return None

    # --------------------------------------------------------
    # Method: traverse
    # Purpose: Displays all student records in the linked list.
    # --------------------------------------------------------
    def traverse(self):
        if self.head is None:
            print("No student records available.")
            return

        temp = self.head

        print("\nStudent Records:")

        while temp is not None:
            display_student(temp.data)
            temp = temp.next


# ------------------------------------------------------------
# Function: display_student
# Purpose : Displays one student record in a readable format.
# ------------------------------------------------------------
def display_student(student):
    print()
    print("Student ID:", student["student_id"])
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Year Level:", student["year_level"])


# ------------------------------------------------------------
# Function: get_non_empty_input
# Purpose : Gets input from the user and prevents blank entries.
# ------------------------------------------------------------
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("Input cannot be empty. Please try again.")


# ------------------------------------------------------------
# Function: add_student
# Purpose : Gets student information and adds it to the linked list.
# ------------------------------------------------------------
def add_student(student_list):
    student_id = get_non_empty_input("Enter Student ID: ")

    # Prevent duplicate Student ID
    if student_list.search(student_id) is not None:
        print("Student ID already exists.")
        return

    name = get_non_empty_input("Enter Student Name: ")
    course = get_non_empty_input("Enter Course: ")
    year_level = get_non_empty_input("Enter Year Level: ")

    student_record = {
        "student_id": student_id,
        "name": name,
        "course": course,
        "year_level": year_level
    }

    student_list.insert_at_end(student_record)
    print("Student record added successfully.")


# ------------------------------------------------------------
# Function: delete_student
# Purpose : Deletes a student record using Student ID.
# ------------------------------------------------------------
def delete_student(student_list):
    student_id = get_non_empty_input("Enter Student ID to delete: ")

    deleted = student_list.delete_by_value(student_id)

    if deleted:
        print("Student record deleted successfully.")
    else:
        print("Student record not found.")


# ------------------------------------------------------------
# Function: search_student
# Purpose : Searches and displays a student record using Student ID.
# ------------------------------------------------------------
def search_student(student_list):
    student_id = get_non_empty_input("Enter Student ID to search: ")

    student = student_list.search(student_id)

    if student is not None:
        print("\nStudent Found:")
        display_student(student)
    else:
        print("Student record not found.")


# ------------------------------------------------------------
# Function: display_menu
# Purpose : Displays the menu options.
# ------------------------------------------------------------
def display_menu():
    print("\n========================================")
    print("STUDENT RECORD MANAGEMENT SYSTEM")
    print("Using Singly Linked List")
    print("========================================")
    print("[1] Add Student Record")
    print("[2] Delete Student Record")
    print("[3] Search Student Record")
    print("[4] Display All Student Records")
    print("[5] Check if List is Empty")
    print("[6] Clear All Records")
    print("[7] Exit")
    print("========================================")


# ------------------------------------------------------------
# Function: load_sample_records
# Purpose : Adds three sample records for testing.
# ------------------------------------------------------------
def load_sample_records(student_list):
    sample_students = [
        {
            "student_id": "2026-001",
            "name": "Juan Dela Cruz",
            "course": "BSIT",
            "year_level": "1st Year"
        },
        {
            "student_id": "2026-002",
            "name": "Maria Santos",
            "course": "BSCS",
            "year_level": "2nd Year"
        },
        {
            "student_id": "2026-003",
            "name": "Pedro Reyes",
            "course": "BSCpE",
            "year_level": "3rd Year"
        }
    ]

    for student in sample_students:
        student_list.insert_at_end(student)


# ============================================================
# Main Program
# ============================================================

def main():
    student_list = SinglyLinkedList()

    # Load at least 3 sample student records for testing
    load_sample_records(student_list)

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(student_list)

        elif choice == "2":
            delete_student(student_list)

        elif choice == "3":
            search_student(student_list)

        elif choice == "4":
            student_list.traverse()

        elif choice == "5":
            if student_list.is_empty():
                print("The student list is empty.")
            else:
                print("The student list is not empty.")

        elif choice == "6":
            student_list.make_null()
            print("All student records have been cleared.")

        elif choice == "7":
            print("Program ended. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
