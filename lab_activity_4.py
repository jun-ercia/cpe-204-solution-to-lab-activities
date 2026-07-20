# ============================================================
# Program Title : Undo and Redo Text Editor Using Array Stack
# Purpose       : This program applies Stack ADT in a simple
#                 text editor with undo and redo operations.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Your Name
# ============================================================


class ArrayStack:

    def __init__(self, max_size):
        # Validate the maximum stack size
        if not isinstance(max_size, int):
            raise TypeError("Maximum size must be an integer.")

        if max_size <= 0:
            raise ValueError("Maximum size must be greater than zero.")

        # Maximum number of elements allowed in the stack
        self.MAX = max_size

        # Create an empty array with fixed size
        self.stack = [None] * self.MAX

        # TOP is -1 when the stack is empty
        self.TOP = -1

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the stack has no elements.
    # --------------------------------------------------------
    def is_empty(self):
        return self.TOP == -1

    # --------------------------------------------------------
    # Method: is_full
    # Purpose: Checks if the stack is already full.
    # --------------------------------------------------------
    def is_full(self):
        return self.TOP == self.MAX - 1

    # --------------------------------------------------------
    # Method: push
    # Purpose: Adds a new item to the top of the stack.
    # --------------------------------------------------------
    def push(self, value):

        # Check for stack overflow
        if self.is_full():
            raise OverflowError("Stack Overflow. The stack is already full.")

        # Move TOP upward
        self.TOP += 1

        # Store the value at the top position
        self.stack[self.TOP] = value

    # --------------------------------------------------------
    # Method: pop
    # Purpose: Removes and returns the top item of the stack.
    # --------------------------------------------------------
    def pop(self):

        # Check for stack underflow
        if self.is_empty():
            raise IndexError(
                "Stack Underflow. Cannot pop from an empty stack."
            )

        # Get the top item
        item = self.stack[self.TOP]

        # Clear the removed position
        self.stack[self.TOP] = None

        # Move TOP downward
        self.TOP -= 1

        return item

    # --------------------------------------------------------
    # Method: peek
    # Purpose: Returns the top item without removing it.
    # --------------------------------------------------------
    def peek(self):

        if self.is_empty():
            raise IndexError(
                "Cannot peek because the stack is empty."
            )

        return self.stack[self.TOP]

    # --------------------------------------------------------
    # Method: size
    # Purpose: Returns the number of elements in the stack.
    # --------------------------------------------------------
    def size(self):
        return self.TOP + 1

    # --------------------------------------------------------
    # Method: display
    # Purpose: Returns all text entries in the order they
    #          were added.
    # --------------------------------------------------------
    def display(self):

        if self.is_empty():
            return ""

        current_text = ""

        # Display entries from bottom to top so that they
        # appear in the order they were entered.
        for i in range(self.TOP + 1):

            if current_text != "":
                current_text += " "

            current_text += str(self.stack[i])

        return current_text

    # --------------------------------------------------------
    # Method: clear
    # Purpose: Removes all elements from the stack.
    # --------------------------------------------------------
    def clear(self):

        for i in range(self.TOP + 1):
            self.stack[i] = None

        self.TOP = -1


# ------------------------------------------------------------
# Function: display_menu
# Purpose : Displays the available program options.
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
# Function: main
# Purpose : Controls the menu-driven application.
# ------------------------------------------------------------
def main():

    try:
        # Maximum number of text entries allowed
        MAX_SIZE = 100

        # Create two array-based stack objects
        undo_stack = ArrayStack(MAX_SIZE)
        redo_stack = ArrayStack(MAX_SIZE)

    except (TypeError, ValueError) as error:
        print("Stack creation error:", error)
        return

    while True:

        try:
            display_menu()

            # Convert the input into an integer
            choice = int(input("Enter your choice: "))

            # ------------------------------------------------
            # Option 1: Add Text
            # ------------------------------------------------
            if choice == 1:

                if undo_stack.is_full():
                    print(
                        "Text editor is full. "
                        "Cannot add more text."
                    )
                    continue

                text = input("Enter text to add: ").strip()

                # Prevent blank text
                if text == "":
                    print("Text cannot be blank.")

                else:
                    try:
                        undo_stack.push(text)

                        # A new action clears the redo history
                        redo_stack.clear()

                        print("Text added successfully.")

                    except OverflowError as error:
                        print(error)

            # ------------------------------------------------
            # Option 2: Undo Last Text
            # ------------------------------------------------
            elif choice == 2:

                try:
                    removed_text = undo_stack.pop()
                    redo_stack.push(removed_text)

                    print("Undo completed.")
                    print("Removed text:", removed_text)

                except IndexError:
                    print("Nothing to undo.")

                except OverflowError as error:
                    print("Undo error:", error)

            # ------------------------------------------------
            # Option 3: Redo Last Text
            # ------------------------------------------------
            elif choice == 3:

                try:
                    restored_text = redo_stack.pop()
                    undo_stack.push(restored_text)

                    print("Redo completed.")
                    print("Restored text:", restored_text)

                except IndexError:
                    print("Nothing to redo.")

                except OverflowError as error:
                    print("Redo error:", error)

            # ------------------------------------------------
            # Option 4: View Current Text
            # ------------------------------------------------
            elif choice == 4:

                if undo_stack.is_empty():
                    print("No text available.")

                else:
                    print("Current Text:")
                    print(undo_stack.display())

            # ------------------------------------------------
            # Option 5: View Last Text
            # ------------------------------------------------
            elif choice == 5:

                try:
                    print(
                        "Last text entered:",
                        undo_stack.peek()
                    )

                except IndexError:
                    print("No last text available.")

            # ------------------------------------------------
            # Option 6: Check if Text Editor Is Empty
            # ------------------------------------------------
            elif choice == 6:

                if undo_stack.is_empty():
                    print("The text editor is empty.")

                else:
                    print("The text editor is not empty.")

            # ------------------------------------------------
            # Option 7: Display Number of Text Entries
            # ------------------------------------------------
            elif choice == 7:

                print(
                    "Number of text entries:",
                    undo_stack.size()
                )

            # ------------------------------------------------
            # Option 8: Clear All Text
            # ------------------------------------------------
            elif choice == 8:

                undo_stack.clear()
                redo_stack.clear()

                print("All text has been cleared.")

            # ------------------------------------------------
            # Option 9: Exit Program
            # ------------------------------------------------
            elif choice == 9:

                print("Program ended. Thank you!")
                break

            # ------------------------------------------------
            # Invalid menu number
            # ------------------------------------------------
            else:
                print(
                    "Invalid menu choice. "
                    "Please enter a number from 1 to 9."
                )

        # Handles letters, symbols, decimal numbers, and blanks
        except ValueError:
            print(
                "Invalid input. Please enter a whole number "
                "from 1 to 9."
            )

        # Handles Ctrl+C and interrupted input
        except KeyboardInterrupt:
            print("\nProgram interrupted by the user.")
            print("Program ended. Thank you!")
            break

        # Handles an unexpected end of input
        except EOFError:
            print("\nNo more input was received.")
            print("Program ended. Thank you!")
            break

        # Handles other unexpected errors
        except Exception as error:
            print("An unexpected error occurred:", error)


# Main program starts here
if __name__ == "__main__":
    main()
