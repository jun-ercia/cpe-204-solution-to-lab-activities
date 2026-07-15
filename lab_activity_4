# ============================================================
# Program Title : Undo and Redo Text Editor Using Stack
# Purpose       : This program applies Stack ADT in a simple
#                 text editor with undo and redo operations.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Your Name
# ============================================================


# ------------------------------------------------------------
# Class: Stack
# Purpose: Represents a stack and its basic operations.
# ------------------------------------------------------------
class Stack:

    def __init__(self):
        # This list will store the stack elements
        self.items = []

    # --------------------------------------------------------
    # Method: push
    # Purpose: Adds an item to the top of the stack.
    # --------------------------------------------------------
    def push(self, value):
        self.items.append(value)

    # --------------------------------------------------------
    # Method: pop
    # Purpose: Removes and returns the top item from the stack.
    # --------------------------------------------------------
    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    # --------------------------------------------------------
    # Method: peek
    # Purpose: Returns the top item without removing it.
    # --------------------------------------------------------
    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the stack has no elements.
    # --------------------------------------------------------
    def is_empty(self):
        return len(self.items) == 0

    # --------------------------------------------------------
    # Method: size
    # Purpose: Returns the number of elements in the stack.
    # --------------------------------------------------------
    def size(self):
        return len(self.items)

    # --------------------------------------------------------
    # Method: display
    # Purpose: Displays all items in the stack in the order
    #          they were added.
    # --------------------------------------------------------
    def display(self):
        if self.is_empty():
            return ""

        return " ".join(self.items)

    # --------------------------------------------------------
    # Method: clear
    # Purpose: Removes all elements from the stack.
    # --------------------------------------------------------
    def clear(self):
        self.items.clear()


# ------------------------------------------------------------
# Function: get_non_blank_input
# Purpose : Prevents the user from entering blank text.
# ------------------------------------------------------------
def get_non_blank_input(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("Input cannot be blank. Please try again.")


# ------------------------------------------------------------
# Function: display_menu
# Purpose : Displays the main menu.
# ------------------------------------------------------------
def display_menu():
    print("\n========================================")
    print("UNDO AND REDO TEXT EDITOR")
    print("Using Stack ADT")
    print("========================================")
    print("[1] Add Text")
    print("[2] Undo Last Text")
    print("[3] Redo Last Text")
    print("[4] View Current Text")
    print("[5] View Last Text")
    print("[6] Check if Text Editor is Empty")
    print("[7] Display Number of Text Entries")
    print("[8] Clear All Text")
    print("[9] Exit")
    print("========================================")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

# Stack for storing current text actions
undo_stack = Stack()

# Stack for storing removed text actions during undo
redo_stack = Stack()

while True:
    display_menu()

    choice = input("Enter your choice: ").strip()

    # --------------------------------------------------------
    # Option 1: Add Text
    # --------------------------------------------------------
    if choice == "1":
        text = get_non_blank_input("Enter text to add: ")

        # Add the new text to the undo stack
        undo_stack.push(text)

        # Clear redo stack because a new action was made
        redo_stack.clear()

        print("Text added successfully.")

    # --------------------------------------------------------
    # Option 2: Undo Last Text
    # --------------------------------------------------------
    elif choice == "2":
        if undo_stack.is_empty():
            print("Nothing to undo.")
        else:
            removed_text = undo_stack.pop()

            # Move removed text to redo stack
            redo_stack.push(removed_text)

            print("Undo completed.")
            print("Removed text:", removed_text)

    # --------------------------------------------------------
    # Option 3: Redo Last Text
    # --------------------------------------------------------
    elif choice == "3":
        if redo_stack.is_empty():
            print("Nothing to redo.")
        else:
            restored_text = redo_stack.pop()

            # Move restored text back to undo stack
            undo_stack.push(restored_text)

            print("Redo completed.")
            print("Restored text:", restored_text)

    # --------------------------------------------------------
    # Option 4: View Current Text
    # --------------------------------------------------------
    elif choice == "4":
        if undo_stack.is_empty():
            print("No text available.")
        else:
            print("Current Text:")
            print(undo_stack.display())

    # --------------------------------------------------------
    # Option 5: View Last Text
    # --------------------------------------------------------
    elif choice == "5":
        last_text = undo_stack.peek()

        if last_text is None:
            print("No last text available.")
        else:
            print("Last text entered:", last_text)

    # --------------------------------------------------------
    # Option 6: Check If Text Editor Is Empty
    # --------------------------------------------------------
    elif choice == "6":
        if undo_stack.is_empty():
            print("The text editor is empty.")
        else:
            print("The text editor is not empty.")

    # --------------------------------------------------------
    # Option 7: Display Number of Text Entries
    # --------------------------------------------------------
    elif choice == "7":
        print("Number of text entries:", undo_stack.size())

    # --------------------------------------------------------
    # Option 8: Clear All Text
    # --------------------------------------------------------
    elif choice == "8":
        undo_stack.clear()
        redo_stack.clear()

        print("All text has been cleared.")

    # --------------------------------------------------------
    # Option 9: Exit Program
    # --------------------------------------------------------
    elif choice == "9":
        print("Program ended. Thank you!")
        break

    # --------------------------------------------------------
    # Invalid Menu Choice
    # --------------------------------------------------------
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
