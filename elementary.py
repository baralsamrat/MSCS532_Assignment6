class Array:
    """A simple implementation of a dynamic array."""
    def __init__(self):
        self.data = []

    def insert(self, value):
        """Insert a value at the end of the array."""
        self.data.append(value)  # O(1) average time complexity

    def delete(self, index):
        """Delete a value at a specific index."""
        if 0 <= index < len(self.data):
            self.data.pop(index)  # O(n) time complexity due to shifting elements
        else:
            raise IndexError("Index out of bounds.")

    def access(self, index):
        """Access a value at a specific index."""
        if 0 <= index < len(self.data):
            return self.data[index]  # O(1) time complexity
        else:
            raise IndexError("Index out of bounds.")

    def display(self):
        """Display the current elements in the array."""
        return self.data


class Stack:
    """A simple implementation of a stack using a list."""
    def __init__(self):
        self.data = []

    def push(self, value):
        """Push a value onto the stack."""
        self.data.append(value)  # O(1)

    def pop(self):
        """Pop a value off the stack."""
        if not self.is_empty():
            return self.data.pop()  # O(1)
        raise IndexError("Pop from an empty stack.")

    def peek(self):
        """Return the top value of the stack without removing it."""
        if not self.is_empty():
            return self.data[-1]  # O(1)
        raise IndexError("Peek from an empty stack.")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.data) == 0


class Queue:
    """A simple implementation of a queue using a list."""
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        """Add a value to the end of the queue."""
        self.data.append(value)  # O(1)

    def dequeue(self):
        """Remove and return the front value from the queue."""
        if not self.is_empty():
            return self.data.pop(0)  # O(n) due to shifting elements
        raise IndexError("Dequeue from an empty queue.")

    def front(self):
        """Return the front value of the queue without removing it."""
        if not self.is_empty():
            return self.data[0]  # O(1)
        raise IndexError("Front from an empty queue.")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.data) == 0


class Node:
    """Node class for singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """A simple implementation of a singly linked list."""
    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert a value at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head  # O(1)
        self.head = new_node  # O(1)

    def delete(self, value):
        """Delete a value from the list."""
        current = self.head
        if current and current.value == value:
            self.head = current.next  # O(1)
            return
        while current:
            if current.next and current.next.value == value:
                current.next = current.next.next  # O(n)
                return
            current = current.next
        raise ValueError("Value not found in the list.")

    def traverse(self):
        """Return a list of values in the linked list."""
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values


def main():
    """Main function to interact with user."""
    data_structures = {
        "1": "Array",
        "2": "Stack",
        "3": "Queue",
        "4": "Singly Linked List"
    }

    while True:
        print("\nSelect a data structure to work with:")
        for key, value in data_structures.items():
            print(f"{key}: {value}")
        print("0: Exit")

        choice = input("Enter your choice: ")
        
        if choice == "0":
            print("Exiting...")
            break

        if choice == "1":
            array = Array()
            while True:
                action = input("\nArray Operations:\n1: Insert\n2: Delete\n3: Access\n4: Display\n0: Back\nChoose an action: ")
                if action == "0":
                    break
                elif action == "1":
                    value = int(input("Enter value to insert: "))
                    array.insert(value)
                elif action == "2":
                    index = int(input("Enter index to delete: "))
                    try:
                        array.delete(index)
                    except IndexError as e:
                        print(e)
                elif action == "3":
                    index = int(input("Enter index to access: "))
                    try:
                        print(f"Value at index {index}: {array.access(index)}")
                    except IndexError as e:
                        print(e)
                elif action == "4":
                    print("Array:", array.display())
        
        elif choice == "2":
            stack = Stack()
            while True:
                action = input("\nStack Operations:\n1: Push\n2: Pop\n3: Peek\n0: Back\nChoose an action: ")
                if action == "0":
                    break
                elif action == "1":
                    value = int(input("Enter value to push: "))
                    stack.push(value)
                elif action == "2":
                    try:
                        print(f"Popped value: {stack.pop()}")
                    except IndexError as e:
                        print(e)
                elif action == "3":
                    try:
                        print(f"Top value: {stack.peek()}")
                    except IndexError as e:
                        print(e)

        elif choice == "3":
            queue = Queue()
            while True:
                action = input("\nQueue Operations:\n1: Enqueue\n2: Dequeue\n3: Front\n0: Back\nChoose an action: ")
                if action == "0":
                    break
                elif action == "1":
                    value = int(input("Enter value to enqueue: "))
                    queue.enqueue(value)
                elif action == "2":
                    try:
                        print(f"Dequeued value: {queue.dequeue()}")
                    except IndexError as e:
                        print(e)
                elif action == "3":
                    try:
                        print(f"Front value: {queue.front()}")
                    except IndexError as e:
                        print(e)

        elif choice == "4":
            linked_list = SinglyLinkedList()
            while True:
                action = input("\nLinked List Operations:\n1: Insert\n2: Delete\n3: Traverse\n0: Back\nChoose an action: ")
                if action == "0":
                    break
                elif action == "1":
                    value = int(input("Enter value to insert: "))
                    linked_list.insert(value)
                elif action == "2":
                    value = int(input("Enter value to delete: "))
                    try:
                        linked_list.delete(value)
                    except ValueError as e:
                        print(e)
                elif action == "3":
                    print("Linked List:", linked_list.traverse())

# Performance Analysis
def performance_analysis():
    """Analyze the time complexity of each data structure's operations."""
    print("\n--- Performance Analysis ---")
    
    print("\n1. Array:")
    print("   - Insert: O(1) (average), O(n) (worst-case if resizing is needed)")
    print("   - Delete: O(n) (due to shifting elements)")
    print("   - Access: O(1)")

    print("\n2. Stack:")
    print("   - Push: O(1)")
    print("   - Pop: O(1)")
    print("   - Peek: O(1)")

    print("\n3. Queue:")
    print("   - Enqueue: O(1)")
    print("   - Dequeue: O(n) (due to shifting elements)")
    print("   - Front: O(1)")

    print("\n4. Singly Linked List:")
    print("   - Insert: O(1) (at head), O(n) (at tail or arbitrary position)")
    print("   - Delete: O(n)")
    print("   - Traverse: O(n)")

    print("\n--- Trade-offs between Arrays and Linked Lists ---")
    print("1. Arrays:")
    print("   - Pros: Fast access, cache-friendly.")
    print("   - Cons: Expensive insertions/deletions, resizing overhead.")

    print("\n2. Linked Lists:")
    print("   - Pros: Efficient insertions/deletions, no resizing needed.")
    print("   - Cons: Slower access, higher memory overhead due to pointers.")

    print("\n--- Efficiency in Specific Scenarios ---")
    print("1. Use Arrays when:")
    print("   - You need fast access by index.")
    print("   - The number of elements is known and stable.")
    
    print("\n2. Use Stacks when:")
    print("   - You need LIFO access (e.g., backtracking).")

    print("\n3. Use Queues when:")
    print("   - You need FIFO access (e.g., task scheduling).")

    print("\n4. Use Linked Lists when:")
    print("   - Frequent insertions/deletions are needed, and order matters.")

if __name__ == "__main__":
    main()
    performance_analysis()
