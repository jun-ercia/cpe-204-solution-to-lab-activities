# ============================================================
# Laboratory Activity 10 - Problem 2
# Music Playlist Manager Using Doubly Linked List
# ============================================================


class Song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # --------------------------------------------------------
    # Check if playlist is empty
    # --------------------------------------------------------
    def is_empty(self):
        return self.head is None

    # --------------------------------------------------------
    # Add a song at the end
    # --------------------------------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)

        # If playlist is empty
        if self.is_empty():
            self.head = new_node
            return

        # Find the last node
        current = self.head

        while current.next is not None:
            current = current.next

        # Connect the new node
        current.next = new_node
        new_node.prev = current

    # --------------------------------------------------------
    # Delete song using Song ID
    # --------------------------------------------------------
    def delete_by_id(self, song_id):
        if self.is_empty():
            print("Playlist is empty.")
            return

        current = self.head

        while current is not None:

            if current.data.song_id == song_id:

                # Case 1: Node is the first node
                if current.prev is None:
                    self.head = current.next

                    if self.head is not None:
                        self.head.prev = None

                # Case 2: Node is in the middle or at the end
                else:
                    current.prev.next = current.next

                    if current.next is not None:
                        current.next.prev = current.prev

                print("Song deleted successfully.")
                return

            current = current.next

        print("Song ID not found.")

    # --------------------------------------------------------
    # Search song using Song ID
    # --------------------------------------------------------
    def search(self, song_id):
        current = self.head

        while current is not None:

            if current.data.song_id == song_id:
                print("Song found:")
                self.display_song(current.data)
                return current

            current = current.next

        print("Song ID not found.")
        return None

    # --------------------------------------------------------
    # Display playlist forward
    # --------------------------------------------------------
    def display_forward(self):
        if self.is_empty():
            print("Playlist is empty.")
            return

        print("Playlist Forward:")
        print("HEAD → ", end="")

        current = self.head

        while current is not None:

            song = current.data

            print(
                f"[{song.song_id} | "
                f"{song.title} | "
                f"{song.artist} | "
                f"{song.duration}]",
                end=""
            )

            if current.next is not None:
                print(" ⇄ ", end="")
            else:
                print(" → NULL")

            current = current.next

    # --------------------------------------------------------
    # Display playlist backward
    # --------------------------------------------------------
    def display_backward(self):
        if self.is_empty():
            print("Playlist is empty.")
            return

        # Find the last node
        current = self.head

        while current.next is not None:
            current = current.next

        print("Playlist Backward:")
        print("TAIL → ", end="")

        while current is not None:

            song = current.data

            print(
                f"[{song.song_id} | "
                f"{song.title} | "
                f"{song.artist} | "
                f"{song.duration}]",
                end=""
            )

            if current.prev is not None:
                print(" ⇄ ", end="")
            else:
                print(" → NULL")

            current = current.prev

    # --------------------------------------------------------
    # View first song
    # --------------------------------------------------------
    def view_first(self):
        if self.is_empty():
            print("Playlist is empty.")
            return

        print("First Song:")
        self.display_song(self.head.data)

    # --------------------------------------------------------
    # View last song
    # --------------------------------------------------------
    def view_last(self):
        if self.is_empty():
            print("Playlist is empty.")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        print("Last Song:")
        self.display_song(current.data)

    # --------------------------------------------------------
    # Clear playlist
    # --------------------------------------------------------
    def clear(self):
        self.head = None
        print("Playlist cleared successfully.")

    # --------------------------------------------------------
    # Helper method for displaying one song
    # --------------------------------------------------------
    def display_song(self, song):
        print("Song ID :", song.song_id)
        print("Title   :", song.title)
        print("Artist  :", song.artist)
        print("Duration:", song.duration)


# ============================================================
# Menu
# ============================================================

def display_menu():
    print()
    print("========================================")
    print("MUSIC PLAYLIST MANAGER")
    print("Doubly Linked List Application")
    print("========================================")
    print("[1] Add Song")
    print("[2] Delete Song by ID")
    print("[3] Search Song")
    print("[4] Display Playlist Forward")
    print("[5] Display Playlist Backward")
    print("[6] View First Song")
    print("[7] View Last Song")
    print("[8] Check if Playlist is Empty")
    print("[9] Clear Playlist")
    print("[10] Exit")
    print("========================================")


# ============================================================
# Main Program
# ============================================================

playlist = DoublyLinkedList()

while True:

    display_menu()

    choice = input("Enter your choice: ")

    # --------------------------------------------------------
    # Add Song
    # --------------------------------------------------------
    if choice == "1":

        print()

        song_id = input("Enter Song ID: ")
        title = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = input("Enter Duration: ")

        # Check if Song ID already exists
        current = playlist.head
        duplicate = False

        while current is not None:
            if current.data.song_id == song_id:
                duplicate = True
                break

            current = current.next

        if duplicate:
            print("Song ID already exists.")

        else:
            new_song = Song(
                song_id,
                title,
                artist,
                duration
            )

            playlist.insert_at_end(new_song)

            print("Song added successfully.")

    # --------------------------------------------------------
    # Delete Song
    # --------------------------------------------------------
    elif choice == "2":

        print()

        song_id = input("Enter Song ID to delete: ")

        playlist.delete_by_id(song_id)

    # --------------------------------------------------------
    # Search Song
    # --------------------------------------------------------
    elif choice == "3":

        print()

        song_id = input("Enter Song ID to search: ")

        playlist.search(song_id)

    # --------------------------------------------------------
    # Display Playlist Forward
    # --------------------------------------------------------
    elif choice == "4":

        print()

        playlist.display_forward()

    # --------------------------------------------------------
    # Display Playlist Backward
    # --------------------------------------------------------
    elif choice == "5":

        print()

        playlist.display_backward()

    # --------------------------------------------------------
    # View First Song
    # --------------------------------------------------------
    elif choice == "6":

        print()

        playlist.view_first()

    # --------------------------------------------------------
    # View Last Song
    # --------------------------------------------------------
    elif choice == "7":

        print()

        playlist.view_last()

    # --------------------------------------------------------
    # Check if Empty
    # --------------------------------------------------------
    elif choice == "8":

        print()

        if playlist.is_empty():
            print("Playlist is empty.")
        else:
            print("Playlist is not empty.")

    # --------------------------------------------------------
    # Clear Playlist
    # --------------------------------------------------------
    elif choice == "9":

        print()

        if playlist.is_empty():
            print("Playlist is already empty.")
        else:
            playlist.clear()

    # --------------------------------------------------------
    # Exit
    # --------------------------------------------------------
    elif choice == "10":

        print()
        print("Exiting Music Playlist Manager.")
        break

    # --------------------------------------------------------
    # Invalid menu choice
    # --------------------------------------------------------
    else:

        print()
        print("Invalid choice. Please enter 1 to 10.")


# ============================================================
# Guide Questions
# ============================================================

# 1. Why is a doubly linked list suitable for a music playlist?
# A doubly linked list is suitable for a music playlist because each
# song can be connected to both the previous song and the next song.
# This allows users to move forward and backward through the playlist.

# 2. What happens to the prev and next pointers when a song is added?
# When a new song is added at the end, the previous last node's next
# pointer is connected to the new node. The new node's prev pointer
# is connected to the previous last node.

# 3. What happens to the prev and next pointers when a song is deleted?
# When a song is deleted, the previous node's next pointer is connected
# to the next node, and the next node's prev pointer is connected to
# the previous node. This removes the deleted node from the list.

# 4. Why is it easier to display backward in a doubly linked list than
# in a singly linked list?
# A doubly linked list has a prev pointer in every node. This allows
# direct movement from the current node to the previous node. A singly
# linked list only has a next pointer.

# 5. What is the role of the head pointer?
# The head pointer stores the reference to the first node of the
# doubly linked list. It is used as the starting point when accessing
# or traversing the playlist.
