class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        # TODO: add value to stack
        pass

    def pop(self):
        # TODO: remove and return top value
        pass

    def peek(self):
        # TODO: return top value without removing
        pass

    def is_empty(self):
        # TODO: return True if empty
        pass

    def size(self):
        # TODO: return number of items
        pass

    def display(self):
        # TODO: display stack contents
        pass

    def clear(self):
        # TODO: remove all items
        pass


text = input("Enter text: ")

if text.strip() == "":
    print("Input cannot be blank. Please try again.")
else:
    original_text = text

    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()

    stack = Stack()

    # TODO:
    # Push every character of cleaned_text into the stack

    reversed_text = ""

    # TODO:
    # Pop characters until the stack is empty
    # Add each popped character to reversed_text

    print("Original Text:", original_text)
    print("Cleaned Text:", cleaned_text)
    print("Reversed Text:", reversed_text)

    # TODO:
    # Compare cleaned_text and reversed_text
