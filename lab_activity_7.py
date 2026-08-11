# ============================================================
# Program Title : Palindrome Checker Using Stack and Queue
# Purpose       : Checks whether text is a palindrome using
#                 Stack ADT and Queue ADT.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Your Name
# ============================================================


# ============================================================
# STACK CLASS
# ============================================================

class Stack:
    def __init__(self):
        self.items = []

    # Add an item to the top of the stack
    def push(self, value):
        self.items.append(value)

    # Remove and return the top item
    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    # Return the top item without removing it
    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the number of items
    def size(self):
        return len(self.items)

    # Display stack contents
    def display(self):
        return self.items

    # Remove all items from the stack
    def clear(self):
        self.items.clear()


# ============================================================
# QUEUE CLASS
# ============================================================

class Queue:
    def __init__(self):
        self.items = []

    # Add an item at the rear of the queue
    def enqueue(self, value):
        self.items.append(value)

    # Remove and return the front item
    def dequeue(self):
        if self.is_empty():
            return None

        return self.items.pop(0)

    # Return the front item without removing it
    def peek(self):
        if self.is_empty():
            return None

        return self.items[0]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the number of items
    def size(self):
        return len(self.items)

    # Display queue contents
    def display(self):
        return self.items

    # Remove all items from the queue
    def clear(self):
        self.items.clear()


# ============================================================
# INPUT FUNCTION
# ============================================================

def get_text():

    while True:
        text = input("Enter text: ")

        if text.strip() == "":
            print("Input cannot be blank. Please try again.")
        else:
            return text


# ============================================================
# PROBLEM 1
# PALINDROME CHECKER USING STACK
# ============================================================

def palindrome_using_stack():

    print()
    print("PALINDROME CHECKER USING STACK")
    print("----------------------------------------")

    original_text = get_text()

    # Remove spaces and convert to lowercase
    cleaned_text = original_text.replace(" ", "").lower()

    stack = Stack()

    # Push every character into the stack
    for character in cleaned_text:
        stack.push(character)

    # Use required stack operations
    stack.size()
    stack.peek()
    stack.display()

    reversed_text = ""

    # Pop characters to create reversed text
    while not stack.is_empty():
        reversed_text += stack.pop()

    print()
    print("Original Text:", original_text)
    print("Cleaned Text:", cleaned_text)
    print("Reversed Text:", reversed_text)

    # Compare cleaned and reversed text
    if cleaned_text == reversed_text:
        print("Result: The text is a palindrome.")
    else:
        print("Result: The text is not a palindrome.")

    stack.clear()


# ============================================================
# PROBLEM 2
# PALINDROME CHECKER USING QUEUE
# ============================================================

def palindrome_using_queue():

    print()
    print("PALINDROME CHECKER USING QUEUE")
    print("----------------------------------------")

    original_text = get_text()

    # Remove spaces and convert to lowercase
    cleaned_text = original_text.replace(" ", "").lower()

    queue = Queue()

    # Enqueue every character
    for character in cleaned_text:
        queue.enqueue(character)

    # Use required queue operations
    queue.size()
    queue.peek()
    queue.display()

    index = len(cleaned_text) - 1

    is_palindrome = True

    # Dequeue characters from the front and compare
    # them with characters starting from the end
    while not queue.is_empty():

        character = queue.dequeue()

        if character != cleaned_text[index]:
            is_palindrome = False
            break

        index -= 1

    print()
    print("Original Text:", original_text)
    print("Cleaned Text:", cleaned_text)

    if is_palindrome:
        print("Result: The text is a palindrome.")
    else:
        print("Result: The text is not a palindrome.")

    queue.clear()


# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    print()
    print("========================================")
    print("PALINDROME CHECKER")
    print("Using Stack and Queue")
    print("========================================")
    print("[1] Check Palindrome Using Stack")
    print("[2] Check Palindrome Using Queue")
    print("[3] Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        palindrome_using_stack()

    elif choice == "2":

        palindrome_using_queue()

    elif choice == "3":

        print()
        print("Program terminated.")
        break

    else:

        print()
        print("Invalid choice. Please enter a valid option.")
