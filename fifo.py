# coding=utf-8

class FIFO1(object):

    def __init__(self, size=5):
        self.size = size
        self.tail = -1
        self.head = 0
        self.cursize = 0
        self.my_queue = [None] * size

    def __str__(self):
        i = self.head
        string = "["
        for j in range(self.cursize-1):
            string = string + str(self.my_queue[i]) + ", "
            i = (i + 1) % self.size
        string = string + str(self.my_queue[i]) + "]"
        return string

    def push(self, data):
        if self.isFull():
            print("Больше нет места")
        else:
            self.tail = (self.tail + 1) % self.size
            self.my_queue[self.tail] = data
            self.cursize += 1

    def pop(self):
        if self.isEmpty():
            print("Очередь пуста!")
        else:
            data = self.my_queue[self.head]
            self.head = (self.head + 1) % self.size
            self.cursize -= 1
            return data

    def isEmpty(self):
        return self.cursize == 0

    def isFull(self):
        return self.cursize == self.size

    def printQueue(self):
        if self.isEmpty():
            print("Очередь пуста!")
        else:
            i = self.head
            for j in range(self.length()):
                print(str(self.my_queue[i]) + " "),
                i = (i + 1) % self.size
            print

    def length(self):
        return self.cursize

    def clear(self):

        i = self.head
        for j in range(self.length()):
            self.my_queue[i] = None
            i = (i + 1) % self.size

        self.tail = 5
        self.head = 0
        self.cursize = 0


class FIFO2(object):

    def __init__(self, size=5):
        self.size = size
        self.tail = 0
        self.head = 0
        self.my_queue = [None] * size

    def __str__(self):
        i = self.head
        string = "["
        for j in range(self.length()-1):
            string = string + str(self.my_queue[i]) + ", "
            i = (i + 1) % self.size
        string = string + str(self.my_queue[i]) + "]"
        return string

    def push(self, data):
        if self.my_queue[self.tail] is not None:
            print("Больше нет места")
        else:
            self.my_queue[self.tail] = data
            self.tail = (self.tail + 1) % self.size

    def pop(self):
        if self.head is None:
            print("Очередь пуста!")
        else:
            data = self.my_queue[self.head]
            self.my_queue[self.head] = None
            self.head = (self.head + 1) % self.size
            return data

    def printQueue(self):
        i = self.head
        for j in range(self.length()):
            print(str(self.my_queue[i]) + " "),
            i = (i + 1) % self.size
        print

    def length(self):
        if self.tail > self.head:
            return self.tail-self.head
        elif self.tail < self.head:
            return self.size - self.head + self.tail
        elif self.my_queue[self.tail] is not None:
            return self.size
        else:
            return 0

    def clear(self):

        i = self.head
        for j in range(self.length()):
            self.my_queue[i] = None
            i = (i + 1) % self.size

        self.tail = 0
        self.head = 0


