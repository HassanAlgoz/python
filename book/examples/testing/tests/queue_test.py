from ds.queue import Queue

def test_init():
    q = Queue()
    assert q.is_empty() == True, "Should be empty after initialization"
    assert q.items == [], "... and has an empty list of items"

def test_enqueue():
    # Arrange: create a queue
    q = Queue()
    
    # Act: add an item to the queue
    q.enqueue('A')
    
    # Assert: check if the item is added to the queue
    assert q.items == ['A'], "Should add item to the queue"
    assert q.is_empty() == False, "Should not be empty after adding an item"

    # Act: add an item to the queue
    q.enqueue('B')
    
    # Assert: check if the item is added to the queue
    assert q.items == ['A', 'B'], "Should add item to the end of the queue"
    
    # Cleanup: free up memory
    del q

def test_dequeue():
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    assert q.dequeue() == 'A', "Should return first-in item (FIFO)"
    assert q.items == ['B'], "Should be removed from the queue"
    assert q.dequeue() == 'B', "Should return next item"
    assert q.is_empty() == True, "Should be empty after all items are dequeued"
    assert q.dequeue() is None, "Should return None on empty queue"

def test_peek():
    q = Queue()
    assert q.peek() is None, "Should return None on empty queue"

    q.enqueue('A')
    assert q.peek() == 'A', "Should return first-in item"
    assert q.items == ['A'], "... without removing it"

    q.enqueue('B')
    assert q.peek() == 'A', "Should still return first-in item, even after adding more items"

def test_is_empty():
    q = Queue()
    assert q.is_empty() == True, "Should be empty after initialization"

    q.enqueue('A')
    assert q.is_empty() == False, "Should not be empty after adding an item"

    q.dequeue()
    assert q.is_empty() == True, "Should be empty after removing the last item"

def test_repr():
    q = Queue()
    assert repr(q) == "[]", "Should return empty list representation if empty"

    q.enqueue('A')
    q.enqueue('B')
    assert repr(q) == "['A', 'B']", "Should return list representation of items"
