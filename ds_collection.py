from abc import ABC, abstractmethod
from typing import Iterable
from random import randint

##### ADTs ######
class Stack(ABC):
    @abstractmethod
    def size(self):
        """Return the number of elements in the stack."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        pass

    @abstractmethod
    def push(self, e):
        """Add an element to the top of the stack."""
        pass

    @abstractmethod
    def top(self):
        """Return (but do not remove) the top element of the stack (None if empty)."""
        pass

    @abstractmethod
    def pop(self):
        """Remove and return the top element of the stack (None if empty)."""
        pass
    
class Queue(ABC):
    @abstractmethod
    def size(self):
        """Return the number of elements in the queue."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        pass

    @abstractmethod
    def enqueue(self, e):
        """Insert an element at the rear of the queue."""
        pass

    @abstractmethod
    def first(self):
        """Return (but do not remove) the first element of the queue (None if empty)."""
        pass

    @abstractmethod
    def dequeue(self):
        """Remove and return the first element of the queue (None if empty)."""
        pass

class Deque(ABC):
    @abstractmethod
    def size(self):
        """Return the number of elements in the deque."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the deque is empty, False otherwise."""
        pass

    @abstractmethod
    def add_first(self, e):
        """Insert an element at the front of the deque."""
        pass

    @abstractmethod
    def add_last(self, e):
        """Insert an element at the rear of the deque."""
        pass

    @abstractmethod
    def remove_first(self):
        """Remove and return the first element of the deque (None if empty)."""
        pass

    @abstractmethod
    def remove_last(self):
        """Remove and return the last element of the deque (None if empty)."""
        pass

    @abstractmethod
    def first(self):
        """Return (but do not remove) the first element of the deque (None if empty)."""
        pass

    @abstractmethod
    def last(self):
        """Return (but do not remove) the last element of the deque (None if empty)."""
        pass

class List(ABC):
    @abstractmethod
    def size(self):
        """Return the number of elements in this list."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the list is empty, False otherwise."""
        pass

    @abstractmethod
    def get(self, i):
        """Return (but do not remove) the element at index i.
        Raise IndexError if index is out of bounds."""
        pass

    @abstractmethod
    def set(self, i, e):
        """Replace the element at index i with e and return the old element.
        Raise IndexError if index is out of bounds."""
        pass

    @abstractmethod
    def add(self, i, e):
        """Insert element e at index i, shifting subsequent elements later.
        Raise IndexError if index is out of bounds."""
        pass

    @abstractmethod
    def remove(self, i):
        """Remove and return the element at index i, shifting subsequent elements earlier.
        Raise IndexError if index is out of bounds."""
        pass

class Position(ABC):
    @abstractmethod
    def get_element(self):
        """Return the element stored at this position.
        Raise an exception if the position is no longer valid.
        """
        pass
    
class PositionalList(ABC):
    @abstractmethod
    def size(self):
        """Return the number of elements in the list."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the list is empty, False otherwise."""
        pass

    @abstractmethod
    def first(self):
        """Return the first Position in the list (or None if empty)."""
        pass

    @abstractmethod
    def last(self):
        """Return the last Position in the list (or None if empty)."""
        pass

    @abstractmethod
    def before(self, p):
        """Return the Position immediately before Position p (or None if p is first).
        Raise ValueError if p is invalid."""
        pass

    @abstractmethod
    def after(self, p):
        """Return the Position immediately after Position p (or None if p is last).
        Raise ValueError if p is invalid."""
        pass

    @abstractmethod
    def add_first(self, e):
        """Insert element e at the front of the list and return its new Position."""
        pass

    @abstractmethod
    def add_last(self, e):
        """Insert element e at the back of the list and return its new Position."""
        pass

    @abstractmethod
    def add_before(self, p, e):
        """Insert element e immediately before Position p and return its new Position.
        Raise ValueError if p is invalid."""
        pass

    @abstractmethod
    def add_after(self, p, e):
        """Insert element e immediately after Position p and return its new Position.
        Raise ValueError if p is invalid."""
        pass

    @abstractmethod
    def set(self, p, e):
        """Replace the element stored at Position p with e and return the old element.
        Raise ValueError if p is invalid."""
        pass

    @abstractmethod
    def remove(self, p):
        """Remove and return the element at Position p, invalidating p.
        Raise ValueError if p is invalid."""
        pass

class Tree(ABC):
    """Abstract base class representing a tree structure with arbitrary number of children."""
    
    @abstractmethod
    def __len__(self) -> int:
        """Return the total number of elements in the tree."""
        pass

    def is_empty(self) -> bool:
        """Return True if the tree is empty."""
        pass

    @abstractmethod
    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        pass

    @abstractmethod
    def positions(self) -> Iterable[Position]:
        """Generate an iteration of the tree's positions."""
        pass

    @abstractmethod
    def root(self) -> Position:
        """Return the root Position of the tree (or None if tree is empty)."""
        pass

    @abstractmethod
    def parent(self, p: Position) -> Position:
        """Return the Position of p's parent (or None if p is root)."""
        pass

    @abstractmethod
    def children(self, p: Position) -> Iterable[Position]:
        """Return an iterable collection containing the children of Position p."""
        pass

    @abstractmethod
    def num_children(self, p: Position) -> int:
        """Return the number of children that Position p has."""
        pass

    @abstractmethod
    def is_internal(self, p: Position) -> bool:
        """Return True if Position p has at least one child."""
        pass

    @abstractmethod
    def is_external(self, p: Position) -> bool:
        """Return True if Position p has no children."""
        pass

    @abstractmethod
    def is_root(self, p: Position) -> bool:
        """Return True if Position p represents the root of the tree."""
        pass

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure,
    in which each node has at most two children.
    """

    @abstractmethod
    def left(self, p: Position) -> Position:
        """Return the Position of p's left child (or None if no child exists)."""
        pass

    @abstractmethod
    def right(self, p: Position) -> Position:
        """Return the Position of p's right child (or None if no child exists)."""
        pass

    @abstractmethod
    def sibling(self, p: Position) -> Position:
        """Return the Position of p's sibling (or None if no sibling exists)."""
        pass

class Entry(ABC):
    """Abstract base class representing a key-value pair."""

    @abstractmethod
    def get_key(self):
        """Return the key stored in this entry."""
        pass

    @abstractmethod
    def get_value(self):
        """Return the value stored in this entry."""
        pass

class PriorityQueue(ABC):
    """Abstract base class representing a priority queue."""

    @abstractmethod
    def __len__(self):
        """Return the number of entries in the priority queue."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the priority queue is empty, False otherwise."""
        pass

    @abstractmethod
    def insert(self, key, value):
        """Insert a key-value pair and return the created entry.
        Raise ValueError if the key is invalid.
        """
        pass

    @abstractmethod
    def min(self):
        """Return (but do not remove) the entry with minimum key.
        Return None if the priority queue is empty.
        """
        pass

    @abstractmethod
    def remove_min(self):
        """Remove and return the entry with minimum key.
        Return None if the priority queue is empty.
        """
        pass

class Map(ABC):
    """Abstract base class representing the Map ADT."""

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of entries in the map."""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the map is empty, and False otherwise."""
        pass

    @abstractmethod
    def get(self, k):
        """Return the value associated with key k, if such an entry exists; otherwise return None."""
        pass

    @abstractmethod
    def put(self, k, v):
        """Insert or replace entry (k, v) in the map.
        If no entry with key k exists, add (k, v) and return None.
        Otherwise, replace the existing value and return the old value.
        """
        pass

    @abstractmethod
    def remove(self, k):
        """Remove the entry with key equal to k and return its value.
        If no such entry exists, return None.
        """
        pass

    @abstractmethod
    def key_set(self) -> Iterable:
        """Return an iterable collection containing all the keys stored in the map."""
        pass

    @abstractmethod
    def values(self) -> Iterable:
        """Return an iterable collection containing all the values stored in the map
        (with repetition if multiple keys map to the same value).
        """
        pass

    @abstractmethod
    def entry_set(self) -> Iterable:
        """Return an iterable collection containing all the key-value entries in the map."""
        pass

class SortedMap(Map):
    """Abstract base class representing a sorted map ADT.
    Extends the Map ADT with additional methods that take advantage
    of the ordering of keys.
    """

    @abstractmethod
    def first_entry(self):
        """Return the entry with the smallest key value, or None if the map is empty."""
        pass

    @abstractmethod
    def last_entry(self):
        """Return the entry with the largest key value, or None if the map is empty."""
        pass

    @abstractmethod
    def ceiling_entry(self, k):
        """Return the entry with the least key value greater than or equal to k,
        or None if no such entry exists.
        """
        pass

    @abstractmethod
    def floor_entry(self, k):
        """Return the entry with the greatest key value less than or equal to k,
        or None if no such entry exists.
        """
        pass
    
    @abstractmethod
    def higher_entry(self, k):
        """Return the entry with the least key value strictly greater than k,
        or None if no such entry exists.
        """
        pass

    @abstractmethod
    def lower_entry(self, k):
        """Return the entry with the greatest key value strictly less than k,
        or None if no such entry exists.
        """
        pass

    @abstractmethod
    def sub_map(self, k1, k2) -> Iterable:
        """Return an iterable collection of all entries with key greater than or equal to k1,
        but strictly less than k2.
        """
        pass


##### Linked Lists ######
class SinglyLinkedList:
    # --------------------- nested Node class ---------------------
    class Node:
        def __init__(self, element, next_node=None):
            self._element = element  # reference to the element stored at this node
            self._next = next_node   # reference to the subsequent node in the list

        def get_element(self):
            return self._element

        def get_next(self):
            return self._next

        def set_next(self, next_node):
            self._next = next_node
    # ----------------- end of nested Node class ------------------

    # --------------------- constructor ---------------------------
    def __init__(self):
        self._head = None           # head node of the list (or None if empty)
        self._tail = None           # last node of the list (or None if empty)
        self._size = 0              # number of nodes in the list

    # --------------------- access methods ------------------------
    def size(self):
        return self._size           # returns the number of elements

    def is_empty(self):
        return self._size == 0      # returns True if the list is empty

    def first(self):
        if self.is_empty():         # returns (but does not remove) the first element
            return None
        return self._head.get_element()

    def last(self):
        if self.is_empty():         # returns (but does not remove) the last element
            return None
        return self._tail.get_element()

    # --------------------- update methods ------------------------
    def add_first(self, e):
        self._head = self.Node(e, self._head)  # create and link a new node
        if self._size == 0:                    # special case: new node becomes tail also
            self._tail = self._head
        self._size += 1                        # increment the size

    def add_last(self, e):
        newest = self.Node(e, None)            # node will eventually be the tail
        if self.is_empty():                    # special case: previously empty list
            self._head = newest
        else:
            self._tail.set_next(newest)        # new node after existing tail
        self._tail = newest                    # new node becomes the tail
        self._size += 1

    def remove_first(self):
        if self.is_empty():                    # nothing to remove
            return None
        answer = self._head.get_element()
        self._head = self._head.get_next()     # will become None if list had only one node
        self._size -= 1
        if self._size == 0:                    # special case as list is now empty
            self._tail = None
        return answer
    
class CircularlyLinkedList:
    # --------------------- nested Node class ---------------------
    class Node:
        def __init__(self, element, next_node=None):
            self._element = element  # reference to the element stored at this node
            self._next = next_node   # reference to the subsequent node in the list

        def get_element(self):
            return self._element

        def get_next(self):
            return self._next

        def set_next(self, next_node):
            self._next = next_node
    # ------------------ end of nested Node class ------------------

    # --------------------- constructor ---------------------------
    def __init__(self):
        self._tail = None                       # we store tail (but not head)
        self._size = 0                          # number of nodes in the list

    # --------------------- access methods ------------------------
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():                     # returns (but does not remove) the first element
            return None
        return self._tail.get_next().get_element()  # the head is *after* the tail

    def last(self):
        if self.is_empty():                     # returns (but does not remove) the last element
            return None
        return self._tail.get_element()

    # --------------------- update methods ------------------------
    def rotate(self):
        if self._tail is not None:              # rotate the first element to the back of the list
            self._tail = self._tail.get_next()  # the old head becomes the new tail

    def add_first(self, e):
        if self._size == 0:
            self._tail = self.Node(e, None)
            self._tail.set_next(self._tail)     # link to itself circularly
        else:
            new_node = self.Node(e, self._tail.get_next())
            self._tail.set_next(new_node)
        self._size += 1

    def add_last(self, e):
        self.add_first(e)                       # insert new element at front of list
        self._tail = self._tail.get_next()      # now new element becomes the tail

    def remove_first(self):
        if self.is_empty():                     # nothing to remove
            return None
        head = self._tail.get_next()
        if head == self._tail:                  # must be the only node left
            self._tail = None
        else:
            self._tail.set_next(head.get_next())  # removes "head" from the list
        self._size -= 1
        return head.get_element()
      
class DoublyLinkedList:
    # --------------------- nested Node class ---------------------
    class Node:
        def __init__(self, element, prev=None, next=None):
            self._element = element             # reference to the element stored at this node
            self._prev = prev                   # reference to the previous node in the list
            self._next = next                   # reference to the next node in the list

        def get_element(self):
            return self._element

        def get_prev(self):
            return self._prev

        def get_next(self):
            return self._next

        def set_prev(self, prev):
            self._prev = prev

        def set_next(self, next):
            self._next = next
    # ------------------ end of nested Node class ------------------

    # ---------------------- constructor ---------------------------
    def __init__(self):
        self._header = self.Node(None)                # header sentinel
        self._trailer = self.Node(None, self._header) # trailer sentinel
        self._header.set_next(self._trailer)          # header is followed by trailer
        self._size = 0                                # number of elements in the list

    # --------------------- access methods ------------------------
    def size(self):
        return self._size                             # number of elements

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():                           # returns (but does not remove) first element
            return None
        return self._header.get_next().get_element()  # first element is beyond header

    def last(self):
        if self.is_empty():                           # returns (but does not remove) last element
            return None
        return self._trailer.get_prev().get_element() # last element is before trailer

    # --------------------- public update methods ------------------------
    def add_first(self, e):
        self._add_between(e, self._header, self._header.get_next())  # place just after header

    def add_last(self, e):
        self._add_between(e, self._trailer.get_prev(), self._trailer)  # place just before trailer

    def remove_first(self):
        if self.is_empty(): return None               # nothing to remove
        return self._remove(self._header.get_next())  # first element is beyond header

    def remove_last(self):
        if self.is_empty(): return None               # nothing to remove
        return self._remove(self._trailer.get_prev()) # last element is before trailer

    # --------------------- private update methods ------------------------
    def _add_between(self, e, predecessor, successor):
        """Adds element e to the list in between the given nodes."""
        newest = self.Node(e, predecessor, successor)  # create and link a new node
        predecessor.set_next(newest)
        successor.set_prev(newest)
        self._size += 1

    def _remove(self, node):
        """Removes the given node from the list and returns its element."""
        predecessor = node.get_prev()
        successor = node.get_next()
        predecessor.set_next(successor)
        successor.set_prev(predecessor)
        self._size -= 1
        return node.get_element()
    

##### Stacks and Queues ######
class ArrayStack(Stack):
    CAPACITY = 1000  # default capacity

    def __init__(self, capacity=CAPACITY):
        self._data = [None] * capacity   # allocate fixed list
        self._t = -1                     # index of top element
        self._capacity = capacity

    def size(self):
        return self._t + 1

    def is_empty(self):
        return self._t == -1

    def push(self, e):
        if self.size() == self._capacity:
            raise Exception("Stack is full")
        self._t += 1
        self._data[self._t] = e

    def top(self):
        if self.is_empty():
            return None
        return self._data[self._t]

    def pop(self):
        if self.is_empty():
            return None
        answer = self._data[self._t]
        self._data[self._t] = None  
        self._t -= 1
        return answer
    
class LinkedStack(Stack):
    def __init__(self):
        self._list = SinglyLinkedList()   # initially empty linked list

    def size(self):
        return self._list.size()

    def is_empty(self):
        return self._list.is_empty()

    def push(self, e):
        self._list.add_first(e)

    def top(self):
        return self._list.first()

    def pop(self):
        return self._list.remove_first()
    
class ArrayQueue(Queue):
    CAPACITY = 1000  # default capacity

    def __init__(self, capacity=CAPACITY):
        self._data = [None] * capacity
        self._f = 0      # index of the front element
        self._size = 0   # number of elements
        self._capacity = capacity

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        if self._size == self._capacity:
            raise Exception("Queue is full")
        avail = (self._f + self._size) % self._capacity  # modular arithmetic
        self._data[avail] = e
        self._size += 1

    def first(self):
        if self.is_empty():
            return None
        return self._data[self._f]

    def dequeue(self):
        if self.is_empty():
            return None
        answer = self._data[self._f]
        self._data[self._f] = None  # help garbage collection
        self._f = (self._f + 1) % self._capacity
        self._size -= 1
        return answer
    
class LinkedQueue(Queue):
    def __init__(self):
        self._list = SinglyLinkedList()   # initially empty linked list

    def size(self):
        return self._list.size()

    def is_empty(self):
        return self._list.is_empty()

    def enqueue(self, e):
        self._list.add_last(e)

    def first(self):
        return self._list.first()

    def dequeue(self):
        return self._list.remove_first()
    

##### Positional Lists ######
class LinkedPositionalList(PositionalList):
    """Implementation of a positional list stored as a doubly linked list."""

    # ---------------- nested Node class ----------------
    class _Node(Position):

        def __init__(self, e, p, n):
            """Create a node storing element e, with links to previous and next nodes."""
            self._element = e    # reference to the element stored at this node
            self._prev = p       # reference to the previous node in the list
            self._next = n       # reference to the subsequent node in the list

        def get_element(self):
            """Return the element stored at this node.
            Raise error if node is no longer valid.
            """
            if self._next is None:  # convention for defunct node
                raise RuntimeError("Position no longer valid")
            return self._element

        def get_prev(self):
            return self._prev

        def get_next(self):
            return self._next

        def set_element(self, e):
            self._element = e

        def set_prev(self, p):
            self._prev = p

        def set_next(self, n):
            self._next = n
    # ---------------- end of nested Node class ----------------

    def __init__(self):
        """Construct a new empty list with header and trailer sentinels."""
        self._header = self._Node(None, None, None)          # header sentinel
        self._trailer = self._Node(None, self._header, None) # trailer is preceded by header
        self._header.set_next(self._trailer)                 # header is followed by trailer
        self._size = 0                                       # number of elements in the list

    def __iter__(self):
        current = self.first()
        while current is not None:
            yield current.get_element()
            current = self._position(current.get_next()) 
    
    # ---------------- protected utilities ----------------
    def _validate(self, p):
        """Validate the position and return it as a node.
        Raise error if the position is invalid.
        """
        if not isinstance(p, self._Node):
            raise RuntimeError("Invalid position")
        
        if p.get_next() is None:  # convention for defunct node
            raise RuntimeError("position is no longer in the list")
        return p

    def _position(self, node):
        """Return the given node as a Position (or None if it is a sentinel)."""
        if node == self._header or node == self._trailer:
            return None  # do not expose user to the sentinels
        return node
    
    

    # ---------------- public accessor methods ----------------
    def size(self):
        """Return the number of elements in the linked list."""
        return self._size
    
    def is_empty(self):
        """Return True if the linked list is empty."""
        return self._size == 0

    def first(self):
        """Return the first Position in the linked list (or None if empty)."""
        return self._position(self._header.get_next())

    def last(self):
        """Return the last Position in the linked list (or None if empty)."""
        return self._position(self._trailer.get_prev())

    def before(self, p):
        """Return the Position immediately before Position p (or None if p is first).
        Raise error if p is invalid.
        """
        node = self._validate(p)
        return self._position(node.get_prev())

    def after(self, p):
        """Return the Position immediately after Position p (or None if p is last).
        Raise error if p is invalid.
        """
        node = self._validate(p)
        return self._position(node.get_next())

    # ---------------- protected utilities ----------------
    def _add_between(self, e, pred, succ):
        """Add element e to the linked list between the given nodes.
        Return the new Position.
        """
        newest = self._Node(e, pred, succ)  # create and link a new node
        pred.set_next(newest)
        succ.set_prev(newest)
        self._size += 1
        return newest

    # ---------------- public update methods ----------------
    def add_first(self, e):
        """Insert element e at the front of the linked list and return its new Position."""
        return self._add_between(e, self._header, self._header.get_next())  # just after the header

    def add_last(self, e):
        """Insert element e at the back of the linked list and return its new Position."""
        return self._add_between(e, self._trailer.get_prev(), self._trailer)  # just before the trailer

    def add_before(self, p, e):
        """Insert element e immediately before Position p and return its new Position.
        Raise error if p is invalid.
        """
        node = self._validate(p)
        return self._add_between(e, node.get_prev(), node)

    def add_after(self, p, e):
        """Insert element e immediately after Position p and return its new Position.
        Raise error if p is invalid.
        """
        node = self._validate(p)
        return self._add_between(e, node, node.get_next())

    def set(self, p, e):
        """Replace the element stored at Position p and return the replaced element.
        Raise error if p is invalid.
        """
        node = self._validate(p)
        answer = node.get_element()
        node.set_element(e)
        return answer

    def remove(self, p):
        """Remove the element stored at Position p and return it (invalidating p).
        Raise error if p is invalid.
        """
        node = self._validate(p)
        predecessor = node.get_prev()
        successor = node.get_next()
        predecessor.set_next(successor)
        successor.set_prev(predecessor)
        self._size -= 1
        answer = node.get_element()
        node.set_element(None)  # help with garbage collection
        node.set_next(None)     # and convention for defunct node
        node.set_prev(None)
        return answer
    

##### Trees ######
class AbstractTree(Tree):
    """An abstract base class providing some functionality of the Tree ABC."""

    def is_empty(self) -> bool:
        """Return True if the tree is empty."""
        return len(self) == 0

    def is_internal(self, p) -> bool:
        """Return True if Position p has at least one child."""
        return self.num_children(p) > 0

    def is_external(self, p) -> bool:
        """Return True if Position p has no children."""
        return self.num_children(p) == 0

    def is_root(self, p) -> bool:
        """Return True if Position p is the root of the tree."""
        return p == self.root()
    
    def depth(self, p) -> int:
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))   
    
    def height(self, p) -> int:
        """Return the height of the subtree rooted at Position p."""
        h = 0                                    # base case if p is external
        for c in self.children(p):
            h = max(h, 1 + self.height(c))
        return h
    
    def __iter__(self):
        """Generate an iteration of the elements stored in the tree."""
        for p in self.positions():
            yield p.get_element()
    
    def positions(self) -> Iterable[Position]:
        """Generate an iteration of the tree's positions using preorder traversal by default."""
        return self.preorder()
    
    def _subtree_preorder(self, p: Position) -> Iterable[Position]:
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p  # for preorder, visit the position before exploring subtrees
        for c in self.children(p):
            yield from self._subtree_preorder(c)
    
    def preorder(self) -> Iterable[Position]:
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            yield from self._subtree_preorder(self.root()) 
  
    def _subtree_postorder(self, p: Position) -> Iterable[Position]:
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            yield from self._subtree_postorder(c)
        yield p  # for postorder, visit position after exploring subtrees
        
    def postorder(self) -> Iterable[Position]:
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            yield from self._subtree_postorder(self.root())
            
    def breadthfirst(self) -> Iterable[Position]:
        """Generate a breadth-first iteration of positions in the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()           # fringe is a queue
            fringe.enqueue(self.root())      # start with the root
            while not fringe.is_empty():
                p = fringe.dequeue()         # remove from front of the queue
                yield p                      # report this position
                for c in self.children(p):
                    fringe.enqueue(c)        # add children to back of queue
       
class AbstractBinaryTree(BinaryTree, AbstractTree):
    """An abstract base class providing some functionality of the BinaryTree ABC."""

    def sibling(self, p: Position) -> Position:
        """Return the Position of p's sibling (or None if no sibling exists)."""
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def num_children(self, p: Position) -> int:
        """Return the number of children of Position p."""
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count

    def children(self, p: Position) -> Iterable[Position]:
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            
    def positions(self) -> Iterable[Position]:
        """Generate an iteration of the tree's positions using inorder traversal by default."""
        return self.inorder()
            
    def _subtree_inorder(self, p: Position) -> Iterable[Position]:
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            yield from self._subtree_inorder(self.left(p))
        yield p
        if self.right(p) is not None:
            yield from self._subtree_inorder(self.right(p))
            
    def inorder(self) -> Iterable[Position]:
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            yield from self._subtree_inorder(self.root())
            
class LinkedBinaryTree(AbstractBinaryTree):
    """Concrete implementation of a binary tree using a node-based, linked structure."""
    # ---------------- nested Node class ----------------
    class _Node(Position):

        def __init__(self, e, parent=None, left=None, right=None):
            self._element = e                  # an element stored at this node
            self._parent = parent              # a reference to the parent node (if any)
            self._left = left                  # a reference to the left child (if any)
            self._right = right                # a reference to the right child (if any)

        # accessor methods
        def get_element(self):
            """Return the element stored at this node.
            Raise error if node is no longer valid.
            """
            if self._parent is self:  # convention for defunct node
                raise RuntimeError("Position no longer valid")
            return self._element

        def get_parent(self):
            return self._parent

        def get_left(self):
            return self._left

        def get_right(self):
            return self._right

        # update methods
        def set_element(self, e):
            self._element = e

        def set_parent(self, parent):
            self._parent = parent

        def set_left(self, left):
            self._left = left

        def set_right(self, right):
            self._right = right
    # ---------------- end of nested Node class ----------------

    # LinkedBinaryTree initializer
    def __init__(self):
        """Constructs an empty binary tree."""
        self._root = None                      # root of the tree
        self._size = 0                         # number of nodes in the tree

    # nonpublic utility
    def _validate(self, p):
        """Validates the position and returns it as a node."""
        if not isinstance(p, self._Node):
            raise RuntimeError("Not valid position type")
        if p.get_parent() is p:
            raise RuntimeError("p is no longer in the tree")
        return p

    def _make_node(self, e, parent=None, left=None, right=None):
        """Factory function to create a new node storing element e."""
        return self._Node(e, parent, left, right)

    # accessor methods
    def __len__(self):
        """Returns the number of nodes in the tree."""
        return self._size
    
    def root(self):
        """Returns the root Position of the tree (or None if tree is empty)."""
        return self._root

    def parent(self, p):
        """Returns the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return node.get_parent()

    def left(self, p):
        """Returns the Position of p's left child (or None if no child exists)."""
        node = self._validate(p)
        return node.get_left()

    def right(self, p):
        """Returns the Position of p's right child (or None if no child exists)."""
        node = self._validate(p)
        return node.get_right()

    # update methods supported by this class
    def add_root(self, e):
        """Places element e at the root of an empty tree and returns its new Position."""
        if self._root is not None:
            raise RuntimeError("Tree is not empty")
        self._root = self._make_node(e, None, None, None)
        self._size = 1
        return self._root

    def add_left(self, p, e):
        """Creates a new left child of Position p storing element e; returns its Position."""
        parent = self._validate(p)
        if parent.get_left() is not None:
            raise RuntimeError("p already has a left child")
        child = self._make_node(e, parent, None, None)
        parent.set_left(child)
        self._size += 1
        return child

    def add_right(self, p, e):
        """Creates a new right child of Position p storing element e; returns its Position."""
        parent = self._validate(p)
        if parent.get_right() is not None:
            raise RuntimeError("p already has a right child")
        child = self._make_node(e, parent, None, None)
        parent.set_right(child)
        self._size += 1
        return child

    def set(self, p, e):
        """Replaces the element at Position p with e and returns the replaced element."""
        node = self._validate(p)
        temp = node.get_element()
        node.set_element(e)
        return temp

    def attach(self, p, t1, t2):
        """Attaches trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if self.is_internal(node):
            raise RuntimeError("p must be a leaf")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root.set_parent(node)
            node.set_left(t1._root)
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root.set_parent(node)
            node.set_right(t2._root)
            t2._root = None
            t2._size = 0

    def remove(self, p):
        """Removes the node at Position p and replaces it with its child, if any."""
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise RuntimeError("p has two children")
        child = node.get_left() if node.get_left() is not None else node.get_right()
        if child is not None:
            child.set_parent(node.get_parent())
        if node == self._root:
            self._root = child
        else:
            parent = node.get_parent()
            if node == parent.get_left():
                parent.set_left(child)
            else:
                parent.set_right(child)
        self._size -= 1
        temp = node.get_element()
        node.set_element(None)
        node.set_left(None)
        node.set_right(None)
        node.set_parent(node)  # our convention for defunct node
        return temp
   
class BalanceableBinaryTree(LinkedBinaryTree):
    """A specialized version of LinkedBinaryTree with support for balancing."""

    # ---------------- nested _BSTNode class ----------------
    class _BSTNode(LinkedBinaryTree._Node):
        """Node of a balanceable binary tree, storing an auxiliary integer field."""

        def __init__(self, e, parent=None, left=None, right=None):
            super().__init__(e, parent, left, right)
            self._aux = 0  # auxiliary data (e.g., height, balance factor, color)

        def get_aux(self):
            """Return the auxiliary value stored at this node."""
            return self._aux

        def set_aux(self, value):
            """Set the auxiliary value stored at this node."""
            self._aux = value

    # ---------------- positional-based auxiliary methods ----------------
    def get_aux(self, p):
        """Return the auxiliary value for position p."""
        node = self._validate(p)
        return node.get_aux()

    def set_aux(self, p, value):
        """Set the auxiliary value for position p."""
        node = self._validate(p)
        node.set_aux(value)

    # ---------------- node factory override ----------------
    def _make_node(self, e, parent=None, left=None, right=None):
        """Create and return a new _BSTNode instance (replaces standard _Node)."""
        return self._BSTNode(e, parent, left, right)

    # ---------------- rotation and restructuring methods ----------------
    def _relink(self, parent, child, make_left_child):
        """Relink a parent node with its oriented child node."""
        if child is not None:
            child.set_parent(parent)
        if make_left_child:
            parent.set_left(child)
        else:
            parent.set_right(child)

    def rotate(self, p):
        """Rotate Position p above its parent."""
        x = self._validate(p)
        y = x.get_parent()
        z = y.get_parent()  # grandparent (possibly None)

        if z is None:
            # x becomes the root of the tree
            self._root = x
            x.set_parent(None)
        else:
            # x becomes direct child of z
            self._relink(z, x, y == z.get_left())

        # Perform rotation (transfer of middle subtree)
        if x == y.get_left():
            self._relink(y, x.get_right(), True)
            self._relink(x, y, False)
        else:
            self._relink(y, x.get_left(), False)
            self._relink(x, y, True)

    def restructure(self, x):
        """Perform a trinode restructuring of Position x with its parent/grandparent."""
        y = self.parent(x)
        z = self.parent(y)

        if (x == self.right(y)) == (y == self.right(z)):
            # Matching alignments: single rotation
            self.rotate(y)
            return y
        else:
            # Opposite alignments: double rotation
            self.rotate(x)
            self.rotate(x)
            return x

##### Priority Queues ######
class AbstractPriorityQueue(PriorityQueue):
    """Abstract base class for a priority queue implementation."""

    # -------------------- nested _PQEntry class --------------------
    class _PQEntry:
        """Lightweight composite to store key-value pairs as entries (protected use)."""

        def __init__(self, key, value):
            self._key = key
            self._value = value
            
        def __repr__(self):
            return f"({self._key}, {self._value})"

        def get_key(self):
            """Return the key stored in this entry."""
            return self._key

        def get_value(self):
            """Return the value stored in this entry."""
            return self._value

        # -------- protected mutators --------
        def _set_key(self, key):
            self._key = key

        def _set_value(self, value):
            self._value = value

        # -------- comparison magic methods --------
        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return self._key != other._key

        def __lt__(self, other):
            return self._key < other._key

        def __le__(self, other):
            return self._key <= other._key

        def __gt__(self, other):
            return self._key > other._key

        def __ge__(self, other):
            return self._key >= other._key
    # ------------------ end of nested _PQEntry class ------------------

    # ------------------------ utility methods ------------------------
    def _check_key(self, key):
        """Validate the key by checking if it supports comparison operations."""
        try:
            key == key
            key < key
        except Exception:
            raise ValueError(
                "Key type must support comparison operations (__eq__ and __lt__ at minimum)"
            )
        return True

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0
    
class UnsortedPriorityQueue(AbstractPriorityQueue):
    """A priority queue implemented with an unsorted positional list."""

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = LinkedPositionalList()

    # ------------------------ nonpublic utility ------------------------
    def _find_min(self):
        """Return Position of entry with minimum key."""
        if self.is_empty():
            return None
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.get_element() < small.get_element():    # compare entries directly via magic methods
                small = walk
            walk = self._data.after(walk)
        return small

    # ------------------------ public methods ------------------------
    def __len__(self):
        """Return the number of entries in the priority queue."""
        return self._data.size()

    def insert(self, key, value):
        """Insert a key-value pair and return the created entry."""
        self._check_key(key)
        newest = self._PQEntry(key, value)
        self._data.add_last(newest)
        return newest

    def min(self):
        """Return but do not remove (key, value) tuple with minimum key, or None if empty."""
        if self.is_empty():
            return None
        p = self._find_min()
        item = p.get_element()
        return item

    def remove_min(self):
        """Remove and return (key, value) tuple with minimum key, or None if empty."""
        if self.is_empty():
            return None
        p = self._find_min()
        item = self._data.remove(p)
        return item
    
class SortedPriorityQueue(AbstractPriorityQueue):
    """A priority queue implemented with a sorted positional list."""

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = LinkedPositionalList()

    def __len__(self):
        """Return the number of entries in the priority queue."""
        return self._data.size()

    def insert(self, key, value):
        """Insert a key-value pair and return the created entry."""
        self._check_key(key)
        newest = self._PQEntry(key, value)
        walk = self._data.last()

        # walk backward looking for a smaller key
        while walk is not None and newest < walk.get_element():
            walk = self._data.before(walk)

        if walk is None:
            # new key is the smallest
            self._data.add_first(newest)
        else:
            # insert after the last smaller or equal key
            self._data.add_after(walk, newest)
        return newest

    def min(self):
        """Return but do not remove the entry with the minimum key (or None if empty)."""
        if self.is_empty():
            return None
        return self._data.first().get_element()

    def remove_min(self):
        """Remove and return the entry with the minimum key (or None if empty)."""
        if self.is_empty():
            return None
        return self._data.remove(self._data.first())
    
class HeapPriorityQueue(AbstractPriorityQueue):
    """A priority queue implemented with a binary heap (array-based)."""

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = []

    # ------------------------ utility methods ------------------------
    def _parent(self, j):
        """Return the index of the parent of j."""
        return (j - 1) // 2

    def _left(self, j):
        """Return the index of the left child of j."""
        return 2 * j + 1

    def _right(self, j):
        """Return the index of the right child of j."""
        return 2 * j + 2

    def _has_left(self, j):
        """Return True if j has a left child."""
        return self._left(j) < len(self)

    def _has_right(self, j):
        """Return True if j has a right child."""
        return self._right(j) < len(self)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of the array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """Move the entry at index j higher to restore heap property."""
        parent = self._parent(j)
        while j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            j = parent
            parent = self._parent(j)

    def _downheap(self, j):
        """Move the entry at index j lower to restore heap property."""
        while self._has_left(j):
            left_index = self._left(j)
            small_child_index = left_index
            if self._has_right(j):
                right_index = self._right(j)
                if self._data[right_index] < self._data[left_index]:
                    small_child_index = right_index
            if self._data[small_child_index] >= self._data[j]:
                break
            self._swap(j, small_child_index)
            j = small_child_index

    # ------------------------ public methods ------------------------
    def __len__(self):
        """Return the number of entries in the priority queue."""
        return len(self._data)

    def insert(self, key, value):
        """Insert a key-value pair and return the created entry."""
        self._check_key(key)
        newest = self._PQEntry(key, value)
        self._data.append(newest)            # add to the end of the list
        self._upheap(len(self._data) - 1)    # fix heap property
        return newest

    def min(self):
        """Return but do not remove the entry with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        return self._data[0]

    def remove_min(self):
        """Remove and return the entry with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        self._swap(0, len(self._data) - 1)   # put min at end
        item = self._data.pop()              # remove it
        if not self.is_empty():
            self._downheap(0)                # fix new root
        return item
    
    
##### Maps ###### 
class AbstractMap(Map):
    """Abstract base class that partially implements the Map interface."""

    # -------------------- nested _MapEntry class --------------------
    class _MapEntry(Entry):
        """Lightweight composite to store key-value pairs as map entries (protected use)."""

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def get_key(self):
            """Return the key stored in this entry."""
            return self._key

        def get_value(self):
            """Return the value stored in this entry."""
            return self._value

        # -------- protected mutators --------
        def _set_key(self, key):
            self._key = key

        def _set_value(self, value):
            old = self._value
            self._value = value
            return old
    # ------------------ end of nested _MapEntry class ------------------

    # ---------------------- concrete methods --------------------------
    def is_empty(self) -> bool:
        """Return True if the map is empty."""
        return len(self) == 0

    def key_set(self) -> Iterable:
        """Return an iterable collection containing all the keys stored in the map."""
        for entry in self.entry_set():
            yield entry.get_key()

    def values(self) -> Iterable:
        """Return an iterable collection containing all the values stored in the map."""
        for entry in self.entry_set():
            yield entry.get_value()
                    
class UnsortedTableMap(AbstractMap):
    """Map implementation using an unsorted list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []   # use a Python list of _MapEntry instances

    # ------------------------- nonpublic utility -------------------------
    def _find_index(self, key):
        """Return index of entry with key (or -1 if not found)."""
        for j in range(len(self._table)):
            if self._table[j].get_key() == key:
                return j
        return -1

    # ------------------------- public methods ----------------------------
    def __len__(self):
        """Return the number of entries in the map."""
        return len(self._table)

    def get(self, k):
        """Return value associated with key k (or None if not found)."""
        j = self._find_index(k)
        if j == -1:
            return None
        return self._table[j].get_value()

    def put(self, k, v):
        """Insert or replace entry (k, v) in the map."""
        j = self._find_index(k)
        if j == -1:
            self._table.append(self._MapEntry(k, v))  # add new entry
            return None
        else:
            return self._table[j]._set_value(v)       # replace existing value

    def remove(self, k):
        """Remove entry with key k and return its value (or None if not found)."""
        j = self._find_index(k)
        if j == -1:
            return None
        # move last entry to 'hole' and pop
        n = len(self._table)
        answer = self._table[j].get_value()
        if j != n - 1:
            self._table[j] = self._table[n - 1]
        self._table.pop()
        return answer

    def entry_set(self):
        """Return an iterable collection of all key-value entries in the map."""
        for entry in self._table:
            yield entry          
   
class AbstractSortedMap(AbstractMap, SortedMap):
    """Abstract base class for a sorted map implementation."""

    # -------------------- nested _MapEntry class --------------------
    class _MapEntry(AbstractMap._MapEntry):
        """Inherits key-value storage and defines comparison magic methods based on keys."""

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return self._key != other._key

        def __lt__(self, other):
            return self._key < other._key

        def __le__(self, other):
            return self._key <= other._key

        def __gt__(self, other):
            return self._key > other._key

        def __ge__(self, other):
            return self._key >= other._key
    # ------------------ end of nested _MapEntry class ------------------

    # ------------------------ utility methods ------------------------
    def _check_key(self, key):
        """Validate that the key supports comparison operations (eq and lt at minimum)."""
        try:
            key == key
            key < key
        except Exception:
            raise ValueError(
                "Key type must support comparison operations (__eq__ and __lt__ at minimum)"
            )
        return True
    
class SortedTableMap(AbstractSortedMap):
    """A sorted map implementation using a simple Python list (table) as storage."""

    def __init__(self):
        """Create a new empty sorted table map."""
        self._table = []  # list of _MapEntry objects

    # -------------------------- Nonpublic utility methods --------------------------
    def _find_index(self, key, low=0, high=None):
        """Return index of the leftmost entry with key >= `key`, or len(table) if not found.

        Uses binary search between indices `low` and `high` (inclusive).
        """
        if high is None:
            high = len(self._table) - 1
        if high < low:
            return low
        mid = (low + high) // 2
        mid_key = self._table[mid].get_key()
        if key == mid_key:
            return mid
        elif key < mid_key:
            return self._find_index(key, low, mid - 1)
        else:
            return self._find_index(key, mid + 1, high)

    def _safe_entry(self, j):
        """Return the entry at index j, or None if j is out of bounds."""
        if 0 <= j < len(self._table):
            return self._table[j]
        return None

    # -------------------------- Map methods --------------------------
    def __len__(self):
        """Return the number of entries in the map."""
        return len(self._table)

    def get(self, k):
        """Return the value associated with key k, or None if not found."""
        j = self._find_index(k)
        if j == len(self._table) or self._table[j].get_key() != k:
            return None
        return self._table[j].get_value()

    def put(self, k, v):
        """Insert or replace entry (k, v) in the map.

        If no entry with key k exists, add (k, v) in sorted order and return None.
        Otherwise, replace the existing value and return the old value.
        """
        self._check_key(k)
        j = self._find_index(k)
        if j < len(self._table) and self._table[j].get_key() == k:
            # Key already exists: replace value
            return self._table[j]._set_value(v)
        # Otherwise insert new entry at the correct position to maintain order
        self._table.insert(j, self._MapEntry(k, v))
        return None

    def remove(self, k):
        """Remove the entry with key equal to k and return its value.

        Return None if no such entry exists.
        """
        j = self._find_index(k)
        if j == len(self._table) or self._table[j].get_key() != k:
            return None
        return self._table.pop(j).get_value()

    def entry_set(self) -> Iterable:
        """Return an iterable collection of all key-value entries in the map."""
        for entry in self._table:
            yield entry

    # -------------------------- SortedMap methods --------------------------
    def first_entry(self):
        """Return the entry with the smallest key, or None if the map is empty."""
        return self._safe_entry(0)

    def last_entry(self):
        """Return the entry with the largest key, or None if the map is empty."""
        return self._safe_entry(len(self._table) - 1)

    def ceiling_entry(self, k):
        """Return the entry with the least key greater than or equal to k, or None if no such entry exists."""
        j = self._find_index(k)
        return self._safe_entry(j)

    def floor_entry(self, k):
        """Return the entry with the greatest key less than or equal to k, or None if no such entry exists."""
        j = self._find_index(k)
        if j == len(self._table) or self._table[j].get_key() != k:
            j -= 1
        return self._safe_entry(j)

    def lower_entry(self, k):
        """Return the entry with the greatest key strictly less than k, or None if no such entry exists."""
        j = self._find_index(k) - 1
        return self._safe_entry(j)

    def higher_entry(self, k):
        """Return the entry with the least key strictly greater than k, or None if no such entry exists."""
        j = self._find_index(k)
        if j < len(self._table) and self._table[j].get_key() == k:
            j += 1
        return self._safe_entry(j)

    def sub_map(self, from_key, to_key):
        """Return an iterable snapshot of entries with from_key <= key < to_key.

        If to_key is None, iteration continues to the end of the table.
        """
        buffer = []
        start = self._find_index(from_key)
        j = start
        while j < len(self._table) and (to_key is None or self._table[j].get_key() < to_key):
            buffer.append(self._table[j])
            j += 1
        return buffer
    
class TreeMap(AbstractSortedMap):
    """A sorted map implementation using a binary search tree."""

    def __init__(self):
        """Create an empty TreeMap."""
        self._tree = LinkedBinaryTree()
        self._tree.add_root(None)  # create a sentinel leaf as root

    # -------------------------- Nonpublic utilities --------------------------
    def _subtree_search(self, p, key):
        """Return Position of key in subtree rooted at p, or last node reached."""
        if self._tree.is_external(p):
            return p                    # key not found; return the final leaf
        entry = p.get_element()
        if key == entry.get_key():
            return p                    # key found; return its position
        elif key < entry.get_key():
            return self._subtree_search(self._tree.left(p), key)        # search left subtree
        else:
            return self._subtree_search(self._tree.right(p), key)       # search right subtree

    def _expand_external(self, p, entry):
        """Convert an external node into an internal node storing entry, with two external children."""
        self._tree.set(p, entry)            # store new entry at p
        self._tree.add_left(p, None)        # add new sentinel leaves as children
        self._tree.add_right(p, None)

    def _tree_min(self, p):
        """Return the Position with minimum key in subtree rooted at p."""
        walk = p
        while not self._tree.is_external(self._tree.left(walk)):
            walk = self._tree.left(walk)
        return walk

    def _tree_max(self, p):
        """Return the Position with maximum key in subtree rooted at p."""
        walk = p
        while not self._tree.is_external(self._tree.right(walk)):
            walk = self._tree.right(walk)
        return walk

    # -------------------------- Map methods --------------------------
    def __len__(self):
        """Return the number of entries in the map."""
        # internal nodes only
        return len(self._tree) // 2

    def get(self, k):
        """Return the value associated with key k, or None if not found."""
        if self.is_empty():
            return None
        p = self._subtree_search(self._tree.root(), k)
        if self._tree.is_external(p):
            return None                         # unsuccessful search
        return p.get_element().get_value()      # match found

    def put(self, k, v):
        """Insert or replace entry (k, v) in the map."""
        self._check_key(k)                 

        p = self._subtree_search(self._tree.root(), k)
        if self._tree.is_external(p):                       # key not found; add new entry  
            self._expand_external(p, self._MapEntry(k, v))
            return None
        old_value = p.get_element()._set_value(v)           # key found; replace value
        return old_value

    def remove(self, k):
        """Remove the entry with key k and return its value, or None if not found."""
        if self.is_empty():
            return None

        p = self._subtree_search(self._tree.root(), k)
        if self._tree.is_external(p):
            return None     # key not found

        old_value = p.get_element().get_value()
        if self._tree.is_internal(self._tree.left(p)) and self._tree.is_internal(self._tree.right(p)):
            # replace with in-order successor
            replacement = self._tree_min(self._tree.right(p))
            self._tree.set(p, replacement.get_element())
            p = replacement  # now remove the successor

        # now p has at most one internal child
        child_sentinel = self._tree.left(p) if self._tree.is_internal(self._tree.right(p)) else self._tree.right(p)
        self._tree.remove(child_sentinel)  
        self._tree.remove(p)
        return old_value

    def entry_set(self):
        """Generate an iteration of all key-value entries in sorted order."""
        for p in self._tree.inorder():
            if self._tree.is_internal(p):
                yield p.get_element()

    # -------------------------- SortedMap methods --------------------------
    def first_entry(self):
        """Return entry with smallest key, or None if empty."""
        if self.is_empty():
            return None
        p = self._tree_min(self._tree.root())
        return p.get_element()

    def last_entry(self):
        """Return entry with largest key, or None if empty."""
        if self.is_empty():
            return None
        p = self._tree_max(self._tree.root())
        return p.get_element()

    def ceiling_entry(self, k):
        """Return entry with least key >= k, or None if no such key."""
        if self.is_empty():
            return None
        p = self._tree.root()
        best = None
        while self._tree.is_internal(p):
            if k == p.get_element().get_key():
                return p.get_element()              # exact match found
            elif k < p.get_element().get_key():
                best = p                            # candidate key >= k
                p = self._tree.left(p)              # move left to find smaller candidate
            else:
                p = self._tree.right(p)             # move right to find larger keys
        return best.get_element() if best else None


    def floor_entry(self, k):
        """Return entry with greatest key <= k, or None if no such key."""
        if self.is_empty():
            return None
        p = self._tree.root()
        best = None
        while self._tree.is_internal(p):
            if k == p.get_element().get_key():
                return p.get_element()              # exact match found
            elif k < p.get_element().get_key():
                p = self._tree.left(p)              # move left to find smaller keys
            else:
                best = p                            # candidate key <= k
                p = self._tree.right(p)             # move right to find larger candidate
        return best.get_element() if best else None
    
    def higher_entry(self, k):
        """Return entry with least key > k, or None if no such key."""
        if self.is_empty():
            return None
        p = self._tree.root()
        best = None
        while self._tree.is_internal(p):
            if k >= p.get_element().get_key():
                # Go right: all keys in left subtree are <= current key
                p = self._tree.right(p)
            else:
                # Candidate (strictly greater than k)
                best = p
                p = self._tree.left(p)
        return best.get_element() if best else None

    def lower_entry(self, k):
        """Return entry with greatest key < k, or None if no such key."""
        if self.is_empty():
            return None
        p = self._tree.root()
        best = None
        while self._tree.is_internal(p):
            if k <= p.get_element().get_key():
                # Go left: all keys in right subtree are >= current key
                p = self._tree.left(p)
            else:
                # Candidate (strictly less than k)
                best = p
                p = self._tree.right(p)
        return best.get_element() if best else None

    def sub_map(self, from_key, to_key):
        """Generate an iteration of entries with from_key <= key < to_key."""
        def recurse(p):
            if self._tree.is_internal(p):
                key = p.get_element().get_key()
                if key > from_key:
                    yield from recurse(self._tree.left(p))       # explore left subtree
                if from_key <= key < to_key:
                    yield p.get_element()                        # report key in range
                if key < to_key:
                    yield from recurse(self._tree.right(p))      # explore right subtree

        if not self.is_empty():
            yield from recurse(self._tree.root())
                  
class AVLTreeMap(TreeMap):
    """A sorted map implementation using an AVL-balanced binary search tree."""

    def __init__(self):
        """Create an empty AVLTreeMap using a balanceable binary tree."""
        self._tree = BalanceableBinaryTree()
        self._tree.add_root(None)  # create a sentinel external root
        self._next_incident_id = 1_000_001 #written by ourselvs

    # -------------------------- Height and balance utilities --------------------------
    def _height(self, p):
        """Return the cached height of the given tree position."""
        return self._tree.get_aux(p)

    def _recompute_height(self, p):
        """Recompute the height of the given position based on its children's heights."""
        self._tree.set_aux(
            p,
            1 + max(
                self._height(self._tree.left(p)),
                self._height(self._tree.right(p))
            ),
        )

    def _is_balanced(self, p):
        """Return True if position p has balance factor between -1 and 1 (inclusive)."""
        return abs(
            self._height(self._tree.left(p)) - self._height(self._tree.right(p))
        ) <= 1

    def _taller_child(self, p):
        """Return the child of p with height no smaller than that of the other child."""
        left_height = self._height(self._tree.left(p))
        right_height = self._height(self._tree.right(p))

        if left_height > right_height:
            return self._tree.left(p)
        elif left_height < right_height:
            return self._tree.right(p)
        else:
            # Equal height children; break tie while matching parent orientation
            if self._tree.is_root(p):
                return self._tree.left(p)
            parent = self._tree.parent(p)
            if p == self._tree.left(parent):
                return self._tree.left(p)
            else:
                return self._tree.right(p)

    # -------------------------- Rebalancing utilities --------------------------
    def _rebalance(self, p):
        """Utility to restore AVL balance up the path from p."""
        while p is not None:
            old_height = self._height(p)
            if not self._is_balanced(p):
                # Imbalance detected -> perform trinode restructuring
                p = self._tree.restructure(self._taller_child(self._taller_child(p)))
                # After restructure, recompute heights of children and self
                self._recompute_height(self._tree.left(p))
                self._recompute_height(self._tree.right(p))
            self._recompute_height(p)
            new_height = self._height(p)
            if old_height == new_height:
                break
            p = self._tree.parent(p)

    def _rebalance_insert(self, p):
        """Rebalancing hook called after insertion."""
        self._rebalance(p)

    def _rebalance_delete(self, p):
        """Rebalancing hook called after deletion."""
        if not self._tree.is_root(p):
            self._rebalance(self._tree.parent(p))

    # -------------------------- Overridden Map methods --------------------------
    def put(self, k, v):
        """Insert or replace entry (k, v) in the map, rebalancing as necessary."""
        self._check_key(k)
        p = self._subtree_search(self._tree.root(), k)

        if self._tree.is_external(p):
            # Key not found: expand external and rebalance
            self._expand_external(p, self._MapEntry(k, v))
            self._rebalance_insert(p)
            return None
        else:
            # Replace existing key (no rebalance needed)
            old_value = p.get_element()._set_value(v)
            return old_value

    def remove(self, k):
        """Remove the entry with key k and return its value, rebalancing as necessary."""
        if self.is_empty():
            return None

        p = self._subtree_search(self._tree.root(), k)
        if self._tree.is_external(p):
            # Key not found
            return None

        old_value = p.get_element().get_value()

        # Case: two internal children → replace with in-order predecessor
        if self._tree.is_internal(self._tree.left(p)) and self._tree.is_internal(self._tree.right(p)):
            replacement = self._tree_max(self._tree.left(p))
            self._tree.set(p, replacement.get_element())
            p = replacement

        # Now p has at most one internal child
        child_sentinel = self._tree.left(p) if self._tree.is_external(self._tree.left(p)) else self._tree.right(p)
        sibling = self._tree.sibling(child_sentinel)

        self._tree.remove(child_sentinel)
        self._tree.remove(p)
        self._rebalance_delete(sibling)

        return old_value           
    
class AbstractHashMap(AbstractMap):
    """Abstract base class representing a hash-based map implementation."""

    # ---------------------------- constructor ----------------------------
    def __init__(self, cap=17, p=109345121):
        """Create an empty hash-table-based map.
        
        cap: initial table capacity (default 17)
        p: a large prime number (default 109345121)
        """
        self._n = 0                         # number of entries in the map
        self._capacity = cap                # length of the table
        self._prime = p                     # prime factor for MAD compression
        self._scale = randint(1, p - 1)     # scaling factor in MAD compression
        self._shift = randint(0, p - 1)     # shift factor in MAD compression
        self._create_table()                # create the initial table structure

    # ---------------------------- public methods ----------------------------
    def __len__(self):
        """Return the number of entries in the map."""
        return self._n

    def get(self, k):
        """Return the value associated with key k (or None if not found)."""
        return self._bucket_get(self._hash_value(k), k)

    def remove(self, k):
        """Remove the entry associated with key k and return its value (or None if not found)."""
        return self._bucket_remove(self._hash_value(k), k)

    def put(self, k, v):
        """Insert or replace entry (k, v) in the map."""
        answer = self._bucket_put(self._hash_value(k), k, v)
        # keep load factor <= 0.5
        if self._n > self._capacity // 2:
            self._resize(2 * self._capacity - 1)
        return answer

    # ---------------------------- private utilities ----------------------------
    def _hash_value(self, k):
        """Compute hash value for key k using MAD compression."""
        return ((abs(hash(k) * self._scale + self._shift) % self._prime) % self._capacity)

    def _resize(self, new_cap):
        """Resize bucket array to capacity new_cap and rehash all entries."""
        old_entries = list(self.entry_set())     # copy existing entries
        self._capacity = new_cap
        self._create_table()                     # based on updated capacity
        self._n = 0                              # will be recomputed during reinsertion
        for e in old_entries:
            self.put(e.get_key(), e.get_value())

    # ----------------------- abstract bucket-level methods -----------------------
    @abstractmethod
    def _create_table(self):
        """Create an empty bucket array."""
        pass

    @abstractmethod
    def _bucket_get(self, h, k):
        """Return value associated with key k in bucket h (or None if not found)."""
        pass

    @abstractmethod
    def _bucket_put(self, h, k, v):
        """Insert or replace (k, v) in bucket h. Return old value if replaced, or None."""
        pass

    @abstractmethod
    def _bucket_remove(self, h, k):
        """Remove and return value associated with key k from bucket h (or None if not found)."""
        pass
    
class ChainHashMap(AbstractHashMap):
    """Hash map implementation using separate chaining with UnsortedTableMap as buckets."""

    # ---------------------------- protected methods ----------------------------
    def _create_table(self):
        """Create an empty bucket array."""
        self._table = [None] * self._capacity     # each slot initially empty

    def _bucket_get(self, h, k):
        """Return value associated with key k in bucket h (or None if not found)."""
        bucket = self._table[h]
        if bucket is None:
            return None
        return bucket.get(k)

    def _bucket_put(self, h, k, v):
        """Insert or replace entry (k, v) in bucket h and return old value if replaced."""
        if self._table[h] is None:
            self._table[h] = UnsortedTableMap()   # create new bucket
        bucket = self._table[h]
        old_size = len(bucket)
        answer = bucket.put(k, v)
        self._n += (len(bucket) - old_size)       # size may have increased
        return answer

    def _bucket_remove(self, h, k):
        """Remove entry having key k from bucket h (if any) and return its value."""
        bucket = self._table[h]
        if bucket is None:
            return None
        old_size = len(bucket)
        answer = bucket.remove(k)
        self._n -= (old_size - len(bucket))       # size may have decreased
        return answer

    # ---------------------------- public methods ----------------------------
    def entry_set(self):
        """Return an iterable collection of all key-value entries in the map."""
        for bucket in self._table:
            if bucket is not None:
                for entry in bucket.entry_set():
                    yield entry
                                        
class ProbeHashMap(AbstractHashMap):
    """Hash map implementation using open addressing with linear probing for collision resolution."""

    # ---------------------------- constructor ----------------------------
    def __init__(self, cap=17, p=109345121):
        """Create a new empty ProbeHashMap with given capacity and prime."""
        super().__init__(cap, p)
        self._DEFUNCT = self._MapEntry(None, None)   # sentinel for deleted locations

    # ---------------------------- protected methods ----------------------------
    def _create_table(self):
        """Create an empty bucket array with length equal to current capacity."""
        self._table = [None] * self._capacity

    def _is_available(self, j):
        """Return True if location j is either empty or the defunct sentinel."""
        return self._table[j] is None or self._table[j] == self._DEFUNCT

    def _find_slot(self, h, k):
        """Return index j of key k, or -(a+1) such that k could be added at index a."""
        avail = -1                         # no slot available (thus far)
        j = h                              # index while scanning table
        while True:
            if self._is_available(j):       # may be either empty or defunct
                if avail == -1:
                    avail = j               # first available slot
                if self._table[j] is None:
                    break                   # search fails immediately if empty
            elif self._table[j].get_key() == k:
                return j                    # successful match
            j = (j + 1) % self._capacity    # keep looking cyclically
            if j == h:
                break                       # stop if we've returned to start
        return -(avail + 1)                 # search has failed; insert at avail

    def _bucket_get(self, h, k):
        """Return value associated with key k in bucket with hash value h, or None if not found."""
        j = self._find_slot(h, k)
        if j < 0:
            return None                     # no match found
        return self._table[j].get_value()

    def _bucket_put(self, h, k, v):
        """Associate key k with value v in bucket with hash value h; return old value if replaced."""
        j = self._find_slot(h, k)
        if j >= 0:                           # key already exists
            return self._table[j]._set_value(v)
        j = -(j + 1)                         # convert to proper insertion index
        self._table[j] = self._MapEntry(k, v)
        self._n += 1
        return None

    def _bucket_remove(self, h, k):
        """Remove entry having key k from bucket with hash value h (if any)."""
        j = self._find_slot(h, k)
        if j < 0:
            return None                      # nothing to remove
        answer = self._table[j].get_value()
        self._table[j] = self._DEFUNCT       # mark slot as deactivated
        self._n -= 1
        return answer

    # ---------------------------- public methods ----------------------------
    def entry_set(self):
        """Return an iterable collection of all key-value entries of the map."""
        for entry in self._table:
            if entry is not None and entry != self._DEFUNCT:
                yield entry