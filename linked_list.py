class Node:
    """
    An object for storing a single node of a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to the next node in linked list
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'<Node data: {self.data}>'


class LinkedList:
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None
        # Maintaing a count attribute allows for len() to be implemented in constant time
        self._count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        takes O(1) time
        """

        return self.head is None

    def __len__(self):
        """
        Returns the number of nodes in the list
        Takes O(1) time
        """

        return self._count
