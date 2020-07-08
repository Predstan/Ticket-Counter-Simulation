class queue:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        return self.size

    def enqueue(self, item):
        newNode = queueNode( item )
        if self.head is None:
            self.head = newNode
            self.tail = self.head

        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        assert not self.isEmpty(), \
            " Queue is Empty"
        if self.head == self.tail:
            self.tail = None
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item
    

class queueNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None



class Queue:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def length(self):
        return len(self.elements)

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        assert self.isEmpty() is not True, \
            " Empty Queue"

        return self.elements.pop(0)


