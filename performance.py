import time
import json
import csv
import os
import random

class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            self.data.pop(index)
        else:
            raise IndexError("Index out of bounds.")

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of bounds.")

    def display(self):
        return self.data


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        raise IndexError("Pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        raise IndexError("Peek from an empty stack.")

    def is_empty(self):
        return len(self.data) == 0

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of bounds.")


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        raise IndexError("Dequeue from an empty queue.")

    def front(self):
        if not self.is_empty():
            return self.data[0]
        raise IndexError("Front from an empty queue.")

    def is_empty(self):
        return len(self.data) == 0

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of bounds.")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        while current:
            if current.next and current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError("Value not found in the list.")

    def traverse(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values

    def access(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of bounds.")
            current = current.next
        return current.value if current else None


def measure_performance(operation, *args):
    """Measure the execution time of a given operation."""
    start_time = time.time()
    operation(*args)
    end_time = time.time()
    return end_time - start_time


def load_data_from_file():
    filename = input("Enter the path to the JSON or CSV file: ").strip()
    if not os.path.isfile(filename):
        print("File not found. Please try again.")
        return load_data_from_file()

    data = []
    if filename.endswith('.json'):
        with open(filename, 'r') as f:
            data = json.load(f)
    elif filename.endswith('.csv'):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.extend(map(int, row))
    else:
        print("Unsupported file format. Please provide a JSON or CSV file.")
        return load_data_from_file()

    return data


def main():
    array = Array()
    stack = Stack()
    queue = Queue()
    linked_list = SinglyLinkedList()

    choice = input("Do you want to input numbers (1) or upload a dataset (2)? ")
    if choice == "1":
        numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    elif choice == "2":
        numbers = load_data_from_file()
    else:
        print("Invalid choice. Exiting.")
        return

    # Check if numbers are enough for array operations
    required_size = 10  # Specify the required size for the example
    if len(numbers) < required_size:
        additional_numbers = [random.randint(0, 100) for _ in range(required_size - len(numbers))]
        numbers.extend(additional_numbers)
        print(f"Added random numbers {additional_numbers} to meet the required size of {required_size}.")

    # Insert numbers into all data structures and measure performance
    insert_times = {}
    for number in numbers:
        insert_times['Array'] = measure_performance(array.insert, number)
        insert_times['Stack'] = measure_performance(stack.push, number)
        insert_times['Queue'] = measure_performance(queue.enqueue, number)
        insert_times['Linked List'] = measure_performance(linked_list.insert, number)

    # Display insert performance
    print("\nInsert Performance (seconds):")
    for structure, time in insert_times.items():
        print(f"{structure}: {time:.6f}")

    # Measure delete performance
    delete_times = {}
    if len(numbers) > 0:
        delete_value = numbers[0]  # Example: delete the first number
        print(f"\nDeleting value: {delete_value}")

        delete_times['Array'] = measure_performance(array.delete, 0)  # Deleting from index 0
        try:
            delete_times['Stack'] = measure_performance(stack.pop)
        except IndexError as e:
            delete_times['Stack'] = str(e)

        try:
            delete_times['Queue'] = measure_performance(queue.dequeue)
        except IndexError as e:
            delete_times['Queue'] = str(e)

        try:
            delete_times['Linked List'] = measure_performance(linked_list.delete, delete_value)
        except ValueError as e:
            delete_times['Linked List'] = str(e)

    # Display delete performance
    print("\nDelete Performance (seconds):")
    for structure, time in delete_times.items():
        print(f"{structure}: {time}")

    # Access times
    access_times = {}
    for i in range(len(numbers)):
        try:
            access_times['Array'] = measure_performance(array.access, i)
        except IndexError:
            access_times['Array'] = float('inf')

        try:
            access_times['Stack'] = measure_performance(stack.access, i) if i < len(stack.data) else float('inf')
        except IndexError:
            access_times['Stack'] = float('inf')

        try:
            access_times['Queue'] = measure_performance(queue.access, i) if i < len(queue.data) else float('inf')
        except IndexError:
            access_times['Queue'] = float('inf')

        try:
            access_times['Linked List'] = measure_performance(linked_list.access, i)
        except IndexError:
            access_times['Linked List'] = float('inf')

    # Display access performance
    print("\nAccess Performance (seconds):")
    for structure, time in access_times.items():
        print(f"{structure}: {time:.6f}")

    # Ranking performance based on average times
    all_times = {
        "Insert": insert_times,
        "Delete": delete_times,
        "Access": access_times
    }

    print("\nPerformance Ranking:")
    for operation, times in all_times.items():
        ranked = sorted(times.items(), key=lambda x: x[1] if isinstance(x[1], float) else float('inf'))
        print(f"\n{operation} Ranking:")
        for rank, (structure, time) in enumerate(ranked):
            print(f"{rank + 1}: {structure} - {time:.6f}")

if __name__ == "__main__":
    main()
