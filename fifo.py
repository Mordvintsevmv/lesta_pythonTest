# coding=utf-8

class FIFO1(object):

    def __init__(self, size=5):
        self.size = size
        self.tail = -1
        self.head = 0
        self.cursize = 0
        self.my_queue = [None] * size

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
        self.tail = -1
        self.head = 0

class FIFO2(object):

    def __init__(self, *args):
        self.my_queue = []
        for data in args:
            self.my_queue.append(data)

    def push(self, data):
        self.my_queue.append(data)

    def pop(self):
        if self.my_queue:
            data = self.my_queue[0]
            for i in range(len(self.my_queue) - 1):
                self.my_queue[i] = self.my_queue[i + 1]

            del self.my_queue[len(self.my_queue) - 1]
            return data

        else:
            return None

    def isEmpty(self):
        return self.my_queue == []


    def printQueue(self):
        for data in self.my_queue:
            print (str(data) + " "),
        print

    def length(self):
        return len(self.my_queue)

    def clear(self):
        for i in range(len(self.my_queue) - 1):
            del self.my_queue[i]

