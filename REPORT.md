https://dillinger.io/

### Part 1: Selection Algorithms

#### 1. Deterministic Algorithm (Median of Medians)

The following implementation of the Median of Medians algorithm efficiently selects the k-th smallest element from an unsorted array in worst-case linear time. The algorithm divides the array into groups of five, computes the median of each group, and recursively finds the median of these medians.


### Part 2: Elementary Data Structures Implementation and Discussion

  
#### 2. Performance Analysis

- **Arrays:** 
  - Insertion: O(1) (amortized), O(n) (if resizing is needed)
  - Deletion: O(n)
  - Access: O(1)

- **Stacks:**
  - Push: O(1)
  - Pop: O(1)
  - Peek: O(1)

- **Queues:**
  - Enqueue: O(1)
  - Dequeue: O(n) (if using an array, O(1) with a linked list)

- **Linked Lists:**
  - Insertion: O(1) (at the head), O(n) (at the tail)
  - Deletion: O(n)
  - Traversal: O(n)

**Trade-offs:**
- Arrays are more memory efficient but can be less flexible than linked lists, which offer dynamic sizing. 
- Stacks are efficiently implemented with both arrays and linked lists; the choice depends on the required operations (e.g., resizing).

#### 3. Discussion

- **Practical Applications:**
  - **Arrays** are useful in situations where fast access is crucial, like in implementing databases or image processing.
  - **Stacks** are widely used in recursion and backtracking algorithms (e.g., parsing expressions).
  - **Queues** are essential in scheduling tasks (e.g., print jobs).
  - **Linked Lists** are suitable for applications requiring frequent insertions/deletions (e.g., music playlists).

- **Scenario Comparisons:**
  - Choose arrays for static datasets where size is known, while linked lists are preferable for dynamic datasets.
  - In multi-threaded applications, stacks and queues ensure safe data access patterns.

