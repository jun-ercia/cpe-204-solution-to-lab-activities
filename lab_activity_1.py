# ============================================================
# Program Title : Basic Array Operations Using OOP
# Purpose       : This program demonstrates basic array operations
#                 using Object-Oriented Programming in Python.
#                 Operations include make_null, is_empty, is_full,
#                 insert, delete, search, and traverse.
# Date Written  : July 1, 2026
# Language      : Python 3
# Written by    : Jun Ercia
# ============================================================


class Array:
    """
    Represents a fixed-size array and provides basic array operations.
    """

    def __init__(self, max_size):
        """
        Initializes the array with a fixed maximum size.

        Args:
            max_size (int): Maximum number of elements the array can store.

        Raises:
            ValueError: If max_size is not a positive integer.
        """

        if not isinstance(max_size, int):
            raise ValueError("Maximum size must be an integer.")

        if max_size <= 0:
            raise ValueError("Maximum size must be greater than zero.")

        self.max_size = max_size
        self.data = [None] * self.max_size
        self.size = 0

    def make_null(self):
        """
        Clears all active elements in the array.
        """

        self.data = [None] * self.max_size
        self.size = 0

    def is_empty(self):
        """
        Checks whether the array has no active elements.

        Returns:
            bool: True if the array is empty, otherwise False.
        """

        return self.size == 0

    def is_full(self):
        """
        Checks whether the array has reached its maximum capacity.

        Returns:
            bool: True if the array is full, otherwise False.
        """

        return self.size == self.max_size

    def insert(self, value, position):
        """
        Inserts a value at the specified position.

        Args:
            value (int): Value to be inserted.
            position (int): Index where the value will be inserted.

        Raises:
            OverflowError: If the array is already full.
            ValueError: If the position is invalid.
        """

        if self.is_full():
            raise OverflowError("Array is full. Cannot insert a new value.")

        if position < 0 or position > self.size:
            raise ValueError(f"Invalid position. Enter a position from 0 to {self.size}.")

        for i in range(self.size - 1, position - 1, -1):
            self.data[i + 1] = self.data[i]

        self.data[position] = value
        self.size += 1

    def delete(self, position):
        """
        Deletes an element from the specified position.

        Args:
            position (int): Index of the element to be deleted.

        Returns:
            int: The deleted value.

        Raises:
            IndexError: If the array is empty.
            ValueError: If the position is invalid.
        """

        if self.is_empty():
            raise IndexError("Array is empty. Cannot delete a value.")

        if position < 0 or position >= self.size:
            raise ValueError(f"Invalid position. Enter a position from 0 to {self.size - 1}.")

        removed_value = self.data[position]

        for i in range(position, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1

        return removed_value

    def search(self, value):
        """
        Searches for a value using linear search.

        Args:
            value (int): Value to search for.

        Returns:
            int: Index of the value if found, otherwise -1.
        """

        for i in range(self.size):
            if self.data[i] == value:
                return i

        return -1

    def traverse(self):
        """
        Returns all active elements in the array.

        Returns:
            list: List of active array elements.
        """

        return self.data[:self.size]


def display_menu():
    """
    Displays the array operations menu.
    """

    print("\n========== ARRAY OPERATIONS MENU ==========")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Traverse")
    print("5. Check if Empty")
    print("6. Check if Full")
    print("7. Make Null")
    print("8. Exit")


def get_integer(prompt):
    """
    Gets a valid integer input from the user.

    Args:
        prompt (str): Input message shown to the user.

    Returns:
        int: Valid integer input.
    """

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_menu_choice():
    """
    Gets a valid menu choice from the user.

    Returns:
        int: Menu choice from 1 to 8.
    """

    while True:
        choice = get_integer("Enter your choice: ")

        if 1 <= choice <= 8:
            return choice

        print("Invalid choice. Please enter a number from 1 to 8.")


def main():
    """
    Runs the array operations program.
    """

    try:
        numbers = Array(5)

        while True:
            display_menu()
            choice = get_menu_choice()

            try:
                if choice == 1:
                    value = get_integer("Enter value to insert: ")
                    position = get_integer("Enter position: ")

                    numbers.insert(value, position)
                    print(f"{value} inserted at position {position}.")

                elif choice == 2:
                    position = get_integer("Enter position to delete: ")

                    removed_value = numbers.delete(position)
                    print(f"{removed_value} deleted from position {position}.")

                elif choice == 3:
                    value = get_integer("Enter value to search: ")

                    index = numbers.search(value)

                    if index != -1:
                        print(f"{value} is found at index {index}.")
                    else:
                        print(f"{value} is not found.")

                elif choice == 4:
                    elements = numbers.traverse()

                    if numbers.is_empty():
                        print("Array is empty.")
                    else:
                        print("Array elements:", elements)

                elif choice == 5:
                    if numbers.is_empty():
                        print("Array is empty.")
                    else:
                        print("Array is not empty.")

                elif choice == 6:
                    if numbers.is_full():
                        print("Array is full.")
                    else:
                        print("Array is not full.")

                elif choice == 7:
                    numbers.make_null()
                    print("Array has been cleared.")

                elif choice == 8:
                    print("Program ended.")
                    break

            except (ValueError, IndexError, OverflowError) as error:
                print("Error:", error)

    except ValueError as error:
        print("Program initialization error:", error)

    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")


if __name__ == "__main__":
    main()
