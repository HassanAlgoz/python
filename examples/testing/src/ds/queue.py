class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove an item from the front of the queue"""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        """Return the item at the front without removing it"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0

    def __repr__(self):
        """Return the underlying list representation"""
        return repr(self.items)