# Customer Service Queue Simulation (List-Based & Linked List–Based)

This project simulates a basic **customer service system** using **two implementations of a queue**:

1. A **list-based queue** using Python's built-in list.
2. A **linked list–based queue** using a custom `ListNode` class.

Customers arrive and join a service queue. Each customer is served in the order they arrive (**FIFO: First-In-First-Out**). Once served, they leave the queue. Both implementations display arriving and served customers, and notify when all customers are served.

---

## Learning Goals

- Understand how queues work using different data structures
- Practice queue operations: enqueue and dequeue
- Compare static (list-based) and dynamic (linked list–based) queue behaviors

---

## Features

- Enqueue customer names as they arrive
- Dequeue and display customers in the order they were added
- Print status messages as customers are served
- Handle edge cases when the queue is empty

---

## Technologies

- Python
- List-based queue (built-in list)
- Linked list queue (custom `ListNode` + `LinkedListQueue` classes)

---

## File Structure

Both queue implementations are included in the same `.py` file:

1. **List-based queue**:
   - Uses two lists: `arriving` and `serving`
   - Enqueues customers with `append()` and dequeues using `pop(0)`
   - Prints arrival and serving messages

2. **Linked list–based queue**:
   - Uses `ListNode` for each customer
   - `LinkedListQueue` class handles enqueue/dequeue logic with pointers
   - Dynamically grows with no fixed capacity

