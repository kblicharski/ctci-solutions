class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        return self.size
