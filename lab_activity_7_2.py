class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        # TODO: add value to rear
        pass

    def dequeue(self):
        # TODO: remove and return front value
        pass

    def peek(self):
        # TODO: return front value
        pass

    def is_empty(self):
        # TODO: return True if empty
        pass

    def size(self):
        # TODO: return number of items
        pass

    def display(self):
        # TODO: display queue
        pass

    def clear(self):
        # TODO: remove all items
        pass


text = input("Enter text: ")

if text.strip() == "":
    print("Input cannot be blank. Please try again.")
else:
    original_text = text
    cleaned_text = text.replace(" ", "").lower()

    queue = Queue()

    # TODO:
    # Enqueue every character

    is_palindrome = True
    index = len(cleaned_text) - 1

    # TODO:
    # Dequeue one character at a time
    # Compare it with cleaned_text[index]
    # Move index backward

    print("Original Text:", original_text)
    print("Cleaned Text:", cleaned_text)

    if is_palindrome:
        print("Result: The text is a palindrome.")
    else:
        print("Result: The text is not a palindrome.")
