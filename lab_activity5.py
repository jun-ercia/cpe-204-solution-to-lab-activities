# ============================================================
# Program Title : Document Editing History System Using Stack ADT
# Purpose       : This program simulates document editing
#                 history using Stack ADT implemented with
#                 a fixed-size array.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Your Name
# ============================================================


class ArrayStack:

    def __init__(self, max_size):
        """Creates an empty fixed-size array stack."""

        if not isinstance(max_size, int):
            raise TypeError("Maximum stack size must be an integer.")

        if max_size <= 0:
            raise ValueError("Maximum stack size must be greater than zero.")

        # Maximum number of editing actions
        self.MAX = max_size

        # Fixed-size array used to store editing actions
        self.stack = [None] * self.MAX

        # top is -1 when the stack is empty
        self.top = -1

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the stack has no elements.
    # --------------------------------------------------------
    def is_empty(self):
        return self.top == -1

    # --------------------------------------------------------
    # Method: is_full
    # Purpose: Checks if the stack has reached its maximum size.
    # --------------------------------------------------------
    def is_full(self):
        return self.top == self.MAX - 1

    # --------------------------------------------------------
    # Method: push
    # Purpose: Adds an editing action to the top of the stack.
    # --------------------------------------------------------
    def push(self, value):

        if self.is_full():
            raise OverflowError(
                "Editing history is full. Cannot add more actions."
            )

        self.top += 1
        self.stack[self.top] = value

    # --------------------------------------------------------
    # Method: pop
    # Purpose: Removes and returns the most recent action.
    # --------------------------------------------------------
    def pop(self):

        if self.is_empty():
            raise IndexError(
                "No editing action available to undo."
            )

        action = self.stack[self.top]

        # Clear the array position occupied by the action
        self.stack[self.top] = None

        self.top -= 1

        return action

    # --------------------------------------------------------
    # Method: peek
    # Purpose: Returns the most recent action without removing it.
    # --------------------------------------------------------
    def peek(self):

        if self.is_empty():
            raise IndexError(
                "No last editing action available."
            )

        return self.stack[self.top]

    # --------------------------------------------------------
    # Method: size
    # Purpose: Returns the number of editing actions.
    # --------------------------------------------------------
    def size(self):
        return self.top + 1

    # --------------------------------------------------------
    # Method: display
    # Purpose: Displays all actions from most recent to oldest.
    # --------------------------------------------------------
    def display(self):

        if self.is_empty():
            raise IndexError(
                "No editing history available."
            )

        for index in range(self.top, -1, -1):
            print(self.stack[index])

    # --------------------------------------------------------
    # Method: clear
    # Purpose: Removes all editing actions from the stack.
    # --------------------------------------------------------
    def clear(self):

        for index in range(self.top + 1):
            self.stack[index] = None

        self.top = -1


# ------------------------------------------------------------
# Function: display_menu
# Purpose : Displays the program menu.
# ------------------------------------------------------------
def display_menu():

    print("\n========================================")
    print("DOCUMENT EDITING HISTORY SYSTEM")
    print("Stack ADT Using Array")
    print("========================================")
    print("[1] Add Editing Action")
    print("[2] Undo Last Action")
    print("[3] View Last Editing Action")
    print("[4] Display All Editing Actions")
    print("[5] Check if Editing History is Empty")
    print("[6] Check if Editing History is Full")
    print("[7] Display Number of Editing Actions")
    print("[8] Clear Editing History")
    print("[9] Exit")
    print("========================================")


# ------------------------------------------------------------
# Function: main
# Purpose : Controls the menu-driven program.
# ------------------------------------------------------------
def main():

    try:
        # Maximum number of actions that can be stored
        MAX_SIZE = 5

        # Create the array-based stack
        editing_history = ArrayStack(MAX_SIZE)

    except (TypeError, ValueError) as error:
        print("Stack creation error:", error)
        return

    while True:

        try:
            display_menu()

            # Convert the user's input to an integer
            choice = int(input("Enter your choice: "))

            # ------------------------------------------------
            # Option 1: Add Editing Action
            # ------------------------------------------------
            if choice == 1:

                if editing_history.is_full():
                    print(
                        "Editing history is full. "
                        "Cannot add more actions."
                    )
                    continue

                action = input(
                    "Enter editing action: "
                ).strip()

                # Prevent blank editing actions
                if action == "":
                    print(
                        "Editing action cannot be blank. "
                        "Please enter a valid action."
                    )
                    continue

                try:
                    editing_history.push(action)
                    print("Editing action added successfully.")

                except OverflowError as error:
                    print(error)

            # ------------------------------------------------
            # Option 2: Undo Last Action
            # ------------------------------------------------
            elif choice == 2:

                try:
                    removed_action = editing_history.pop()

                    print("Undo completed.")
                    print("Removed action:", removed_action)

                except IndexError as error:
                    print(error)

            # ------------------------------------------------
            # Option 3: View Last Editing Action
            # ------------------------------------------------
            elif choice == 3:

                try:
                    last_action = editing_history.peek()

                    print(
                        "Last editing action:",
                        last_action
                    )

                except IndexError as error:
                    print(error)

            # ------------------------------------------------
            # Option 4: Display All Editing Actions
            # ------------------------------------------------
            elif choice == 4:

                try:
                    print("Editing History:")
                    editing_history.display()

                except IndexError as error:
                    print(error)

            # ------------------------------------------------
            # Option 5: Check if History Is Empty
            # ------------------------------------------------
            elif choice == 5:

                if editing_history.is_empty():
                    print("The editing history is empty.")

                else:
                    print(
                        "The editing history is not empty."
                    )

            # ------------------------------------------------
            # Option 6: Check if History Is Full
            # ------------------------------------------------
            elif choice == 6:

                if editing_history.is_full():
                    print("The editing history is full.")

                else:
                    print(
                        "The editing history is not full."
                    )

            # ------------------------------------------------
            # Option 7: Display Number of Actions
            # ------------------------------------------------
            elif choice == 7:

                print(
                    "Number of editing actions:",
                    editing_history.size()
                )

            # ------------------------------------------------
            # Option 8: Clear Editing History
            # ------------------------------------------------
            elif choice == 8:

                editing_history.clear()

                print(
                    "Editing history has been cleared."
                )

            # ------------------------------------------------
            # Option 9: Exit Program
            # ------------------------------------------------
            elif choice == 9:

                print("Program ended. Thank you!")
                break

            # ------------------------------------------------
            # Invalid Menu Number
            # ------------------------------------------------
            else:
                print(
                    "Invalid menu choice. "
                    "Please enter a number from 1 to 9."
                )

        # Handles letters, symbols, decimals, and blank input
        except ValueError:
            print(
                "Invalid input. Please enter a whole number "
                "from 1 to 9."
            )

        # Handles Ctrl+C
        except KeyboardInterrupt:
            print("\nProgram interrupted by the user.")
            print("Program ended. Thank you!")
            break

        # Handles unexpected end of input
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
